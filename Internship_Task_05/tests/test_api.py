
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Running successfully"


def test_valid_user_input():
    payload = {
        "name": "Arun",
        "age": 22,
        "email": "arun@gmail.com"
    }

    response = client.post("/validate", json=payload)

    assert response.status_code == 200
    assert response.json()["name"] == "Arun"
    assert response.json()["age"] == 22


def test_invalid_age():
    payload = {
        "name": "Arun",
        "age": 15,
        "email": "arun@gmail.com"
    }

    response = client.post("/validate", json=payload)

    assert response.status_code == 422


def test_invalid_email():
    payload = {
        "name": "Arun",
        "age": 22,
        "email": "invalid-email"
    }

    response = client.post("/validate", json=payload)

    assert response.status_code == 422


def test_short_name():
    payload = {
        "name": "A",
        "age": 22,
        "email": "arun@gmail.com"
    }

    response = client.post("/validate", json=payload)

    assert response.status_code == 422
