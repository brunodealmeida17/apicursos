from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.schemas import user as schemas_user
from app.database import get_db


router = APIRouter()

@router.get('/user/{user_id}', response_model=schemas_user.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not foud")
    return db_user


@router.get('/users/', response_model=list[schemas_user.User])
def read_users(skip: int = 0, limit : int = 20, db: Session = Depends(get_db)):
    db_user = crud_user.get_users(db, skip=skip, limit=limit)
    return db_user


@router.post("/user/", response_model=schemas_user.User)
def create_user(user: schemas_user.UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db=db, user=user)


@router.put('/user/{user_id}', response_model=schemas_user.User)
def put_user(user_id: int, user: schemas_user.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not foud")
    return db_user

@router.delete('/user/{user_id}', response_model=schemas_user.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not foud")
    
    return db_user


