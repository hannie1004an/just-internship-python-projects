
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, get_db, Base
from app.models import Student
from app.schemas import StudentCreate, StudentResponse


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task 7 - Pytest Unit Testing Suite")


@app.get("/")
def home():
    return {"message": "Task 7 API is running"}


# Create a student
@app.post("/students/", response_model=StudentResponse, status_code=201)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    existing_student = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_student = Student(
        name=student.name,
        department=student.department,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# Retrieve all students
@app.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


# Retrieve a student by ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student
