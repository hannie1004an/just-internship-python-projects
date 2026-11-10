import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI application
app = FastAPI(
    title="Task 4 - FastAPI Server",
    description="A simple API application developed for the Python Developer Internship.",
    version="1.0.0"
)
# Define the JSON request model
class APIRequest(BaseModel):
    name: str
    message: str


# Root endpoint
@app.get("/")
async def home():
    return {
        "message": "Welcome to the Task 4 FastAPI Server!",
        "status": "Running successfully"
    }


# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "API is working correctly"
    }
# POST endpoint to receive JSON data
@app.post("/submit")
async def submit_data(data: APIRequest):
    return {
        "message": "Data received successfully!",
        "name": data.name,
        "user_message": data.message
    }
# Simulated asynchronous API checks

async def check_database():
    await asyncio.sleep(2)
    return {
        "database": "Connected",
        "status": "Success"
    }


async def check_storage():
    await asyncio.sleep(2)
    return {
        "storage": "Available",
        "status": "Success"
    }


async def check_external_service():
    await asyncio.sleep(2)
    return {
        "external_service": "Running",
        "status": "Success"
    }


# Execute all checks concurrently
@app.get("/checks")
async def concurrent_checks():
    results = await asyncio.gather(
        check_database(),
        check_storage(),
        check_external_service()
    )

    return {
        "message": "All concurrent API checks completed",
        "results": results
    }
