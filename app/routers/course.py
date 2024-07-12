from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.crud import course as crud_course
from app.schemas import course as schemas_course
from app.database import get_db


