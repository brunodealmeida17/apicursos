from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    title: str
    description: str
    active: Optional[bool] = True


class CoursesCreate(CourseBase):
    price: float


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True