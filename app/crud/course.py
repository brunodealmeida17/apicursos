from sqlalchemy.orm import Session
from app.models.course import Course
from app.schemas.courses import CoursesCreate


def get_course(db:  Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session, skip: int=0, limit: int=20):
    return db.query(Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: CoursesCreate):
    db_course = db.query(title=course.title, description=course.description, price=course.price)

    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def update_course(db: Session, course_id: int, course: CoursesCreate):
    db_course = get_course(db, course_id)
    
    if db_course:
        db_course.title = course.title
        db_course.description = course.description
        db_course.price = course.price
        db_course.active = course.active

        db.commit()
        db.refresh(db_course)
        return db_course
    return None

def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    
    if db_course:
        db.delete()
        db.refresh()
        return f"course successfully deleted: {db_course.title}"        
    return None