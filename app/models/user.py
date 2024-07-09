from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
 

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, max_length=100, index=True)
    email = Column(String, unique=True, max_length=150, index=True)
    password = Column(String)
    active = Column(Boolean)
