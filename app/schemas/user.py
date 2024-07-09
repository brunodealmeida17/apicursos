from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str


class UserActive(UserBase):
    active: bool


class user(UserBase):
    id: int


    class Config:
        orm_mode = True