from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.crud import course as crud_course
from app.schemas import courses as schemas_course
from app.database import get_db


router = APIRouter()

@router.get('/course/{course_id}', response_model=schemas_course.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud_course.get_course(db, course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail='Course not found')
    return db_course


@router.get('/courses', response_model=list[schemas_course.Course])
def read_courses(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    db_course = crud_course.get_courses(db, skip, limit)
    return db_course


@router.post('/course/',  response_model=schemas_course.Course)
def post_course(course : schemas_course.CoursesCreate, db: Session = Depends(get_db)):
    return crud_course.create_course(db=db, course=course)

    
@router.put('/course/{course_id}', response_model=schemas_course.Course)
def update_course(course_id: int, course: schemas_course.CoursesCreate, db: Session = Depends(get_db)):
    db_course = crud_course.update_course(db=db, course_id=course_id, course=course)
    if db_course is None:
        raise HTTPException(status_code=404, detail='Course not found')
    return db_course


@router.delete('/course/{course_id}', response_model=schemas_course.Course)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud_course.delete_course(db, course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail='Course not found')
    return db_course
    
