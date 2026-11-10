from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "SQLite Database API is running successfully!"


def test_create_user():
    response = client.post(
        "/users/",
        json={
            "name": "Test User",
            "email": "testuser@example.com"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Test User"
    assert response.json()["email"] == "testuser@example.com"


def test_get_users():
    response = client.get("/users/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_record():
    user_response = client.post(
        "/users/",
        json={
            "name": "Record User",
            "email": "recorduser@example.com"
        }
    )

    user_id = user_response.json()["id"]

    response = client.post(
        f"/users/{user_id}/records/",
        json={"data": "My first database record"}
    )

    assert response.status_code == 200
    assert response.json()["data"] == "My first database record"
    assert response.json()["user_id"] == user_id


def test_get_user_records():
    user_response = client.post(
        "/users/",
        json={
            "name": "Records Test",
            "email": "recordstest@example.com"
        }
    )

    user_id = user_response.json()["id"]

    client.post(
        f"/users/{user_id}/records/",
        json={"data": "Sample record"}
    )

    response = client.get(f"/users/{user_id}/records/")

    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_duplicate_email():
    email = "duplicate@example.com"

    client.post(
        "/users/",
        json={"name": "First User", "email": email}
    )

    response = client.post(
        "/users/",
        json={"name": "Second User", "email": email}
    )

    assert response.status_code == 400


def test_record_for_missing_user():
    response = client.post(
        "/users/99999/records/",
        json={"data": "Test record"}
    )

    assert response.status_code == 404