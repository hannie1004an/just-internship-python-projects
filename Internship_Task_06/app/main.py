from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app import models, schemas

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SQLite Relational Integration API",
    description="FastAPI application integrated with SQLite and SQLAlchemy",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "SQLite Database API is running successfully!"}


# Create a new user
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = models.User(
        name=user.name,
        email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# Get all users
@app.get("/users/", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


# Create a record for a user
@app.post("/users/{user_id}/records/", response_model=schemas.RecordResponse)
def create_record(
    user_id: int,
    record: schemas.RecordCreate,
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_record = models.APIRecord(
        data=record.data,
        user_id=user_id
    )

    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return db_record


# Get records belonging to a user
@app.get("/users/{user_id}/records/", response_model=list[schemas.RecordResponse])
def get_user_records(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return db.query(models.APIRecord).filter(
        models.APIRecord.user_id == user_id
    ).all()