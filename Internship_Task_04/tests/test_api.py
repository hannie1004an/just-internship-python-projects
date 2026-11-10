
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Running successfully"


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_submit_endpoint():
    payload = {
        "name": "Sivaranjani",
        "message": "Testing FastAPI"
    }

    response = client.post("/submit", json=payload)

    assert response.status_code == 200
    assert response.json()["name"] == "Sivaranjani"
    assert response.json()["user_message"] == "Testing FastAPI"


def test_concurrent_checks_endpoint():
    response = client.get("/checks")

    assert response.status_code == 200

    data = response.json()
    assert len(data["results"]) == 3
    assert data["results"][0]["status"] == "Success"
    assert data["results"][1]["status"] == "Success"
    assert data["results"][2]["status"] == "Success"
