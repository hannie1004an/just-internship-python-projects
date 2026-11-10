
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


# User database table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    # One user can have many API records
    records = relationship(
        "APIRecord",
        back_populates="user",
        cascade="all, delete-orphan"
    )


# API records database table
class APIRecord(Base):
    __tablename__ = "api_records"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String(500), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    # Connect API record to its user
    user = relationship(
        "User",
        back_populates="records"
    )
