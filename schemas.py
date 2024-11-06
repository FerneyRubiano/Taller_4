# schemas.py
from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: int

    class Config:
        orm_mode = True