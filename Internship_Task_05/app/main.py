
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Create FastAPI application
app = FastAPI(
    title="Task 5 - Input Validation API",
    description="API for validating user input using Pydantic.",
    version="1.0.0"
)


# Define the request model with validation constraints
class UserInput(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=18, le=100)
    email: str = Field(
        pattern=r"^[\w.-]+@[\w.-]+\.\w{2,}$"
    )


# Home endpoint
@app.get("/")
async def home():
    return {
        "message": "Welcome to the Input Validation API!",
        "status": "Running successfully"
    }


# Input validation endpoint
@app.post("/validate")
async def validate_user(user: UserInput):
    return {
        "message": "Input validated successfully!",
        "name": user.name,
        "age": user.age,
        "email": user.email
    }
