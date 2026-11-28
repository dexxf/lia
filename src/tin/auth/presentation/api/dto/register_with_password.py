from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class RegisterWithPasswordRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class RegisterWithPasswordResponse(BaseModel):
    auth_id: str
    email: str
    created_at: datetime
