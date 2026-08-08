from app import app

def test_dashboard():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps Pipeline Dashboard" in response.data

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

def test_api_status():
    client = app.test_client()
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert "version" in data
