from pydantic import BaseModel, EmailStr

from app.api.models.fields import PhoneNumber


__all__ = [
    "UserModel",
    "UserSchema",
]


class UserModel(BaseModel):
    username: str
    firstName: str
    lastName: str
    email: EmailStr
    phone: PhoneNumber


class UserSchema(UserModel):
    id: int

    class Config:
        orm_mode = True
