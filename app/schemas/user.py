from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str
    active: Optional[bool] = True

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int


    class Config:
        orm_mode = True