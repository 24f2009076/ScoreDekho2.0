from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    full_name: str

class LoginRequest(BaseModel):
    full_name: str
    password: str