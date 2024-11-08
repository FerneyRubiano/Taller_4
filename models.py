from sqlalchemy import Column, Integer, String, UniqueConstraint
from database import Base

class User(Base):
    
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)  # Asegúrate de que sea String

    __table_args__ = (UniqueConstraint('email', name='uq_user_email'),)
