from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: str

class CoursesPrice(CourseBase):
    price: float


class CourseActive(CourseBase):
    active: bool


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True