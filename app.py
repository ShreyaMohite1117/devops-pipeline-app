from flask import Flask, jsonify, render_template_string
import os
import time
import socket
from datetime import datetime

app = Flask(__name__)

START_TIME = time.time()
APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
HOSTNAME = socket.gethostname()  # In Kubernetes, this is the pod name
DEPLOYED_AT = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DevOps Pipeline Dashboard</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #0f172a;
    color: #e2e8f0;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 24px;
  }
  .container { max-width: 720px; width: 100%; }
  .header { text-align: center; margin-bottom: 32px; }
  .header h1 { font-size: 28px; font-weight: 600; margin-bottom: 8px; }
  .header p { color: #94a3b8; font-size: 15px; }
  .status-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #064e3b;
    color: #6ee7b7;
    padding: 8px 20px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 500;
    margin-top: 16px;
  }
  .dot {
    width: 8px; height: 8px;
    background: #34d399;
    border-radius: 50%;
    animation: pulse 2s infinite;
  }
  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
  }
  .card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 20px;
  }
  .card-label {
    font-size: 12px;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
  }
  .card-value {
    font-size: 20px;
    font-weight: 600;
    color: #f1f5f9;
    word-break: break-all;
  }
  .footer {
    text-align: center;
    margin-top: 32px;
    color: #64748b;
    font-size: 13px;
  }
  .footer code {
    background: #1e293b;
    padding: 2px 8px;
    border-radius: 4px;
    color: #93c5fd;
  }
</style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>DevOps Pipeline Dashboard</h1>
      <p>Deployed via Jenkins &rarr; Docker Hub &rarr; Kubernetes</p>
      <div class="status-badge"><span class="dot"></span> All systems healthy</div>
    </div>
    <div class="grid">
      <div class="card">
        <div class="card-label">Version</div>
        <div class="card-value">{{ version }}</div>
      </div>
      <div class="card">
        <div class="card-label">Pod hostname</div>
        <div class="card-value">{{ hostname }}</div>
      </div>
      <div class="card">
        <div class="card-label">Uptime</div>
        <div class="card-value">{{ uptime }}</div>
      </div>
      <div class="card">
        <div class="card-label">Started at</div>
        <div class="card-value">{{ deployed_at }}</div>
      </div>
    </div>
    <div class="footer">
      Health check: <code>/health</code> &middot; API status: <code>/api/status</code>
    </div>
  </div>
</body>
</html>
"""


def get_uptime():
    seconds = int(time.time() - START_TIME)
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours}h {mins}m {secs}s"


@app.route("/")
def dashboard():
    return render_template_string(
        DASHBOARD_HTML,
        version=APP_VERSION,
        hostname=HOSTNAME,
        uptime=get_uptime(),
        deployed_at=DEPLOYED_AT,
    )


@app.route("/health")
def health():
    # Used by Kubernetes liveness/readiness probes
    return jsonify({"status": "healthy"}), 200


@app.route("/api/status")
def api_status():
    return jsonify({
        "message": "Hello from my CI/CD pipeline app!",
        "version": APP_VERSION,
        "hostname": HOSTNAME,
        "uptime": get_uptime(),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
