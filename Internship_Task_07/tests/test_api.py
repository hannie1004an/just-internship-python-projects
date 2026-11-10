
# Test 1: Check home endpoint
def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Task 7 API is running"
    }


# Test 2: Create a student
def test_create_student(client):
    response = client.post(
        "/students/",
        json={
            "name": "Arun Kumar",
            "department": "AI and Data Science",
            "email": "arun@example.com"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Arun Kumar"
    assert response.json()["department"] == "AI and Data Science"


# Test 3: Retrieve all students
def test_get_students(client):
    client.post(
        "/students/",
        json={
            "name": "Priya",
            "department": "Computer Science",
            "email": "priya@example.com"
        }
    )

    response = client.get("/students/")

    assert response.status_code == 200
    assert len(response.json()) == 1


# Test 4: Retrieve student by ID
def test_get_student_by_id(client):
    create_response = client.post(
        "/students/",
        json={
            "name": "Kumar",
            "department": "Information Technology",
            "email": "kumar@example.com"
        }
    )

    student_id = create_response.json()["id"]

    response = client.get(f"/students/{student_id}")

    assert response.status_code == 200
    assert response.json()["email"] == "kumar@example.com"


# Test 5: Check duplicate email error
def test_duplicate_email(client):
    student_data = {
        "name": "Arun",
        "department": "AI and Data Science",
        "email": "arun@example.com"
    }

    client.post("/students/", json=student_data)
    response = client.post("/students/", json=student_data)

    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


# Test 6: Check missing student error
def test_missing_student(client):
    response = client.get("/students/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"


# Test 7: Check invalid student data
def test_invalid_student_data(client):
    response = client.post(
        "/students/",
        json={
            "name": "A",
            "department": "AI",
            "email": "invalid-email"
        }
    )

    assert response.status_code == 422


# Test 8: Check empty student list
def test_empty_student_list(client):
    response = client.get("/students/")

    assert response.status_code == 200
    assert response.json() == []
