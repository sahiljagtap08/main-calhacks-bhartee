from fastapi.testclient import TestClient
from bharteeai.server.api import app

client = TestClient(app)

def test_execute_code():
    response = client.post("/api/execute_code", json={"code": "print('Hello, World!')", "language": "python3"})
    assert response.status_code == 200
    assert "Hello, World!" in response.json()["output"]

def test_get_jobs():
    response = client.get("/api/jobs")
    assert response.status_code == 200
    assert "jobs" in response.json()

def test_apply_for_job():
    response = client.post("/api/apply", json={"job_id": 1})
    assert response.status_code == 200
    assert "message" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}