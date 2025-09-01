from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "TaskFlow API"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_register():
    response = client.post("/auth/register", json={
        "email": "test@test.com",
        "username": "testuser",
        "password": "test123"
    })
    assert response.status_code == 200
    assert "email" in response.json()

