
from pydantic import BaseModel, Field


# Schema for creating a student
class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    department: str = Field(min_length=2, max_length=100)
    email: str = Field(
        regex=r"^[\w.-]+@[\w.-]+\.\w{2,}$"
    )


# Schema for displaying a student
class StudentResponse(BaseModel):
    id: int
    name: str
    department: str
    email: str

    class Config:
        orm_mode = True
