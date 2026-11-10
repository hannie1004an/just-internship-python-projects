
from pydantic import BaseModel, Field


# Schema for creating a user
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: str = Field(
        regex=r"^[\w.-]+@[\w.-]+\.\w{2,}$"
    )


# Schema for displaying a user
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


# Schema for creating an API record
class RecordCreate(BaseModel):
    data: str = Field(min_length=1, max_length=500)


# Schema for displaying an API record
class RecordResponse(BaseModel):
    id: int
    data: str
    user_id: int

    class Config:
        orm_mode = True