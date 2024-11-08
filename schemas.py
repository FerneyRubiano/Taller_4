from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str  # Asegúrate de que sea str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: int

    class Config:
        from_attributes = True
