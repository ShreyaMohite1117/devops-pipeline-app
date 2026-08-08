# DevOps CI/CD Pipeline

An end-to-end CI/CD pipeline that automatically tests, containerizes, deploys, and monitors a Flask application — triggered entirely by a `git push`.

**Flow:** Developer pushes code → GitHub webhook triggers Jenkins → Jenkins runs tests → builds a Docker image → pushes it to Docker Hub → deploys to Kubernetes → Prometheus and Grafana monitor the running pods live.

The deployed app itself is a small live status dashboard showing its own version, which Kubernetes pod served the request, uptime, and deploy time — useful for visibly confirming a successful rollout.

## Screenshots

| Live dashboard | Jenkins pipeline | Grafana monitoring |
|---|---|---|
| ![Dashboard](screenshots/dashboard.png) | ![Jenkins](screenshots/jenkins-success.png) | ![Grafana](screenshots/grafana-metrics.png) |

## Tech stack

| Tool | Purpose |
|---|---|
| Python (Flask) | Sample application |
| pytest | Automated testing |
| Git + GitHub | Version control, webhook trigger |
| Docker | Containerization |
| Docker Hub | Container image registry |
| Jenkins | CI/CD automation |
| ngrok | Exposes local Jenkins to GitHub's webhook |
| Kubernetes | Container orchestration |
| Helm | Installed the monitoring stack |
| Prometheus + Grafana | Metrics collection and dashboards |

## What happens on every push

1. **Checkout** — Jenkins pulls the latest code from GitHub
2. **Test** — runs the pytest suite (`test_app.py`)
3. **Build** — builds a Docker image from the `Dockerfile`
4. **Push** — pushes the image to Docker Hub
5. **Deploy** — applies `deployment.yaml` / `service.yaml` and runs `kubectl rollout restart` so Kubernetes pulls the fresh image and replaces the running pods with zero downtime

## Project structure

```
devops-pipeline-app/
├── app.py              # Flask application
├── test_app.py         # pytest test suite
├── requirements.txt    # Python dependencies
├── Dockerfile           # Container definition
├── Jenkinsfile          # CI/CD pipeline definition
├── deployment.yaml       # Kubernetes Deployment (2 replicas)
├── service.yaml          # Kubernetes Service
└── README.md
```

## Running it locally

**Prerequisites:** Docker Desktop (with Kubernetes enabled), Python 3.12+, Jenkins, kubectl, Helm

```bash
# Run the app directly
pip install -r requirements.txt
python app.py

# Or run it in Docker
docker build -t devops-pipeline-app .
docker run -p 5000:5000 devops-pipeline-app

# Deploy to Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl port-forward svc/devops-pipeline-app-service 5000:5000
```

Visit `http://localhost:5000` and `http://localhost:5000/health`.

## Monitoring

Prometheus + Grafana are installed via Helm (`kube-prometheus-stack`):

```bash
kubectl port-forward svc/monitoring-grafana 3000:80
```

Visit `http://localhost:3000` (username: `admin`) to see live CPU/memory graphs for the running pods.

## Key challenges solved

- **Windows PATH issues** — Jenkins (running as a Windows service) couldn't find `git`, `python`, or `pip` by name; fixed by using full executable paths in the Jenkinsfile.
- **Docker Hub authentication failure** — `docker login --password-stdin` was silently corrupted by a trailing carriage return that Windows' `echo` command adds when piping into stdin. Fixed by passing the password directly via the `-p` flag instead.
- **Minikube crash on Windows** — hit a recurring `update-alternatives: no alternatives for iptables` crash in the Minikube base image. Switched to Docker Desktop's built-in Kubernetes (`kind`-based), which avoided the issue entirely.
- **NodePort not reachable on `kind`-based clusters** — used `kubectl port-forward` instead, which works reliably regardless of cluster type.

## Architecture

```
Developer → GitHub → Jenkins (webhook-triggered)
                        │
                        ├─ Run tests (pytest)
                        ├─ Build Docker image
                        ├─ Push to Docker Hub
                        └─ Deploy to Kubernetes
                                │
                                ├─ App pods (2 replicas, self-healing)
                                └─ Prometheus + Grafana (live monitoring)
```
