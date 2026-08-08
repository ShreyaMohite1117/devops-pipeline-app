# 🚀 DevOps CI/CD Pipeline

An end-to-end DevOps project that demonstrates an automated CI/CD pipeline for a Flask application using **GitHub, Jenkins, Docker, Docker Hub, Kubernetes, Prometheus, and Grafana**.

The pipeline is triggered automatically whenever new code is pushed to GitHub.

---

## 📌 Project Overview

This project implements a complete automated software delivery workflow:

```text
Developer
    ↓
GitHub
    ↓
GitHub Webhook
    ↓
Jenkins
    ↓
Automated Tests
    ↓
Docker Build
    ↓
Docker Hub
    ↓
Kubernetes Deployment
    ↓
Prometheus + Grafana
```
## 📸 Project Screenshots

### 🖥️ Live Application Dashboard

The live dashboard displays the running application's status, version, uptime, deployment information, and the Kubernetes pod serving the request.

<img width="1365" height="767" alt="live_dashboard" src="https://github.com/user-attachments/assets/ba06b81f-164c-45fd-990c-edcf5e342211" />


---

### 🌐 Application Running on Localhost

The Flask application running successfully on the local development environment.

<img width="1365" height="767" alt="localhost_running" src="https://github.com/user-attachments/assets/13a6d378-499c-414d-bea9-0a3d9c7231d2" />


---

### 🐳 Docker Desktop

Docker Desktop showing the containerized application running successfully.

<img width="1365" height="715" alt="docker_desktop" src="https://github.com/user-attachments/assets/8118e510-4a3a-4fd1-aa18-0411161f751a" />

---

### ☸️ Kubernetes

Kubernetes showing the deployed application pods and services.

<img width="1365" height="610" alt="Kubernetes " src="https://github.com/user-attachments/assets/a57eb9c2-4c45-440c-9a5d-ac3f40cd509b" />


---

### ⚙️ Jenkins CI/CD Pipeline

Jenkins pipeline showing the automated CI/CD stages including testing, Docker image creation, Docker Hub push, and Kubernetes deployment.

<img width="1365" height="767" alt="jenkins_build" src="https://github.com/user-attachments/assets/9e8c7eb3-9be9-43b2-9678-8b21c554e526" />

<img width="1365" height="767" alt="jenkins_final" src="https://github.com/user-attachments/assets/58926ee0-a318-4eed-9c26-1e07ab8ea5c2" />


---

### 🔗 GitHub Webhook with ngrok

ngrok exposing the locally running Jenkins server so that GitHub can trigger the Jenkins pipeline through a webhook.

<img width="1098" height="564" alt="ngrok" src="https://github.com/user-attachments/assets/eb7b7ea0-ddbc-4b07-a644-f67aa429eb68" />

---

### 📊 Grafana Monitoring

Grafana dashboard showing monitoring metrics for the running Kubernetes workloads.

<img width="1365" height="767" alt="grafana" src="https://github.com/user-attachments/assets/474d889e-c71d-48de-8da9-670bcdf8a729" />

<img width="1365" height="680" alt="grafana_data" src="https://github.com/user-attachments/assets/9d204b93-ed0d-4eea-9327-a33a066fcdb3" />

---

Whenever a developer pushes new code:

1. GitHub triggers Jenkins using a webhook.
2. Jenkins checks out the latest source code.
3. Automated tests are executed using `pytest`.
4. A Docker image is built.
5. The Docker image is pushed to Docker Hub.
6. The application is deployed to Kubernetes.
7. Kubernetes runs the application using multiple replicas.
8. Prometheus collects monitoring metrics.
9. Grafana provides monitoring dashboards.

---

## ✨ Features

- 🔄 Automated CI/CD pipeline
- 🔗 GitHub webhook integration
- ⚙️ Jenkins Pipeline automation
- 🧪 Automated testing with pytest
- 🐳 Docker containerization
- 📦 Docker Hub image registry
- ☸️ Kubernetes deployment
- 🔁 Two application replicas
- 📊 Prometheus monitoring
- 📈 Grafana dashboards
- 🌐 ngrok for exposing local Jenkins
- ❤️ Application health endpoint
- 🚀 Automated Kubernetes rollout
- 📋 Live application deployment dashboard

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Flask | Web application framework |
| pytest | Automated testing |
| Git | Version control |
| GitHub | Source code management |
| GitHub Webhook | CI/CD trigger |
| Jenkins | CI/CD automation |
| Docker | Containerization |
| Docker Hub | Container image registry |
| Kubernetes | Container orchestration |
| kubectl | Kubernetes management |
| Helm | Monitoring stack installation |
| Prometheus | Metrics collection |
| Grafana | Metrics visualization |
| ngrok | Local Jenkins webhook exposure |

---

## 🏗️ Architecture

```text
                         ┌──────────────────┐
                         │    Developer     │
                         └────────┬─────────┘
                                  │
                               git push
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     GitHub       │
                         └────────┬─────────┘
                                  │
                               Webhook
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     Jenkins      │
                         └────────┬─────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
        ┌───────────┐       ┌────────────┐      ┌────────────┐
        │   Test    │       │   Docker   │      │   Deploy   │
        │  pytest   │──────▶│   Build    │─────▶│ Kubernetes │
        └───────────┘       └─────┬──────┘      └─────┬──────┘
                                  │                    │
                                  ▼                    ▼
                           ┌─────────────┐      ┌─────────────┐
                           │ Docker Hub  │      │  App Pods   │
                           └─────────────┘      │ 2 Replicas  │
                                                └──────┬──────┘
                                                       │
                                                       ▼
                                           ┌────────────────────┐
                                           │     Monitoring     │
                                           │                    │
                                           │    Prometheus      │
                                           │         +          │
                                           │      Grafana       │
                                           └────────────────────┘
```

---

## 🔄 CI/CD Pipeline

### 1. Checkout

Jenkins pulls the latest source code from the GitHub repository.

### 2. Test

The application is automatically tested using `pytest`.

```bash
pytest test_app.py
```

### 3. Build

Jenkins builds a Docker image using the project's `Dockerfile`.

```bash
docker build -t devops-pipeline-app .
```

### 4. Push

The generated Docker image is pushed to Docker Hub.

### 5. Deploy

Kubernetes deployment and service configurations are applied.

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

The deployment is restarted so that Kubernetes replaces the running pods with the latest application version.

### 6. Monitor

Prometheus collects metrics from the Kubernetes environment and Grafana provides dashboards for monitoring the running workloads.

---

## 📂 Project Structure

```text
devops-pipeline-app/
│
├── .gitignore
│
├── Dockerfile
│   └── Docker container configuration
│
├── Jenkinsfile
│   └── Jenkins CI/CD pipeline
│
├── README.md
│   └── Project documentation
│
├── app.py
│   └── Flask application
│
├── test_app.py
│   └── Automated test suite
│
├── requirements.txt
│   └── Python dependencies
│
├── deployment.yaml
│   └── Kubernetes Deployment
│
└── service.yaml
    └── Kubernetes Service
```

---

## 🖥️ Application

The project contains a Flask-based application that provides a live deployment status dashboard.

The dashboard displays information such as:

- Application version
- Kubernetes pod serving the request
- Application uptime
- Deployment time
- Current application status

This provides a simple way to verify that the latest deployment has successfully reached the Kubernetes environment.

---

## ❤️ Health Check

The application provides a health endpoint:

```text
http://localhost:5000/health
```

This endpoint can be used to verify that the application is running correctly.

---

# 🚀 Getting Started

## Prerequisites

Install the following tools:

- Python 3.12+
- Git
- Docker Desktop
- Jenkins
- kubectl
- Helm
- Kubernetes
- ngrok

Docker Desktop's built-in Kubernetes environment can be used for local deployment.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/ShreyaMohite1117/devops-pipeline-app.git
```

Navigate to the project:

```bash
cd devops-pipeline-app
```

---

# 🐍 Run the Application Locally

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask application:

```bash
python app.py
```

Open the application:

```text
http://localhost:5000
```

Health check:

```text
http://localhost:5000/health
```

---

# 🐳 Run Using Docker

Build the Docker image:

```bash
docker build -t devops-pipeline-app .
```

Run the container:

```bash
docker run -p 5000:5000 devops-pipeline-app
```

Open:

```text
http://localhost:5000
```

---

# ☸️ Kubernetes Deployment

Apply the Kubernetes deployment:

```bash
kubectl apply -f deployment.yaml
```

Apply the Kubernetes service:

```bash
kubectl apply -f service.yaml
```

Check running pods:

```bash
kubectl get pods
```

Check deployments:

```bash
kubectl get deployments
```

Check services:

```bash
kubectl get services
```

For local access, use:

```bash
kubectl port-forward svc/devops-pipeline-app-service 5000:5000
```

Then open:

```text
http://localhost:5000
```

---

# ⚙️ Jenkins CI/CD

The CI/CD pipeline is defined in:

```text
Jenkinsfile
```

Jenkins executes the pipeline automatically after receiving a GitHub webhook.

### Pipeline stages

```text
Checkout
   ↓
Test
   ↓
Docker Build
   ↓
Docker Hub Push
   ↓
Kubernetes Deploy
   ↓
Application Rollout
```

The Jenkins Pipeline approach allows the CI/CD process to be stored as code alongside the application. Jenkins officially documents `Jenkinsfile`-based Pipeline-as-Code and Docker integration for pipelines. 

---

# 🔗 GitHub Webhook

GitHub is configured to trigger Jenkins whenever new code is pushed.

For a locally running Jenkins server, ngrok can expose Jenkins to the internet.

Start ngrok:

```bash
ngrok http 8080
```

The resulting HTTPS endpoint can be configured as the GitHub repository webhook.

```text
GitHub
   │
   │ Webhook
   ▼
ngrok
   │
   ▼
Jenkins
```

---

# 📊 Monitoring

The project uses:

- Prometheus for metrics collection
- Grafana for visualization

Prometheus and Grafana are installed using Helm.

Install the monitoring stack:

```bash
helm install monitoring prometheus-community/kube-prometheus-stack
```

Check the monitoring components:

```bash
kubectl get pods
```

---

## Grafana

Forward the Grafana service:

```bash
kubectl port-forward svc/monitoring-grafana 3000:80
```

Open:

```text
http://localhost:3000
```

Grafana can be used to monitor Kubernetes workloads and view CPU and memory metrics.

---

# 🧪 Testing

The automated tests are located in:

```text
test_app.py
```

Run the test suite manually:

```bash
pytest
```

Testing is also performed automatically as part of the Jenkins CI/CD pipeline.

---

# 🧩 Key Challenges Solved

## Windows PATH Issues

Jenkins running as a Windows service could not locate tools such as Git, Python, and pip using the normal PATH configuration.

The Jenkins pipeline was configured with the required executable paths.

## Docker Hub Authentication

Credentials were stored securely in the Jenkins Credentials store rather than hardcoded. However, piping the password via `echo %PASSWORD% | docker login --password-stdin` failed silently on Windows — the `echo` command adds a trailing carriage return that corrupts the stdin input, an issue that doesn't occur on Linux. This was resolved by passing the password directly via the `-p` flag instead.

## Minikube Issue on Windows

Minikube encountered an `iptables`-related issue in the Windows environment.

Docker Desktop's built-in Kubernetes environment was used instead.

## Kubernetes Service Access

NodePort access was not reliable in the local Kubernetes environment.

`kubectl port-forward` was therefore used for reliable local application access.

---

# 🎯 Learning Outcomes

This project provided hands-on experience with:

- Continuous Integration
- Continuous Deployment
- Jenkins Pipeline
- GitHub Webhooks
- Docker
- Docker Hub
- Kubernetes
- Kubernetes Deployments
- Kubernetes Services
- Helm
- Prometheus
- Grafana
- Automated Testing
- Containerization
- DevOps Automation
- Application Monitoring

---

# 🔮 Future Improvements

The following improvements can be added in future versions:

- [ ] SonarQube code quality analysis
- [ ] Trivy container vulnerability scanning
- [ ] Automated deployment rollback
- [ ] Git commit-based Docker image tagging
- [ ] Kubernetes readiness probes
- [ ] Kubernetes liveness probes
- [ ] Horizontal Pod Autoscaling
- [ ] Deployment notifications
- [ ] Cloud Kubernetes deployment
- [ ] HTTPS/TLS configuration
- [ ] Secure secret management

---

# 👩‍💻 Author

**Shreya Mohite**

Computer Engineering / Software Engineering

GitHub:  
https://github.com/ShreyaMohite1117

---

# ⭐ Project Summary

This project demonstrates a complete DevOps workflow:

```text
GitHub
   ↓
Webhook
   ↓
Jenkins
   ↓
Automated Testing
   ↓
Docker Build
   ↓
Docker Hub
   ↓
Kubernetes
   ↓
Application Deployment
   ↓
Prometheus
   ↓
Grafana
```

**End-to-end CI/CD + Docker + Kubernetes + Monitoring**

