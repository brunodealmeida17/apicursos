from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate



def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit : int = 20):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, password=user.password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = get_user(db, user_id)
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db_user.password = user.password
        db_user.active = user.active
        db.commit()
        db.refresh(db_user)
        return db_user
    
    return None

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    
    return None


        
