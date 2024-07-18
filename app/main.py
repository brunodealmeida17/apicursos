from fastapi import FastAPI
from app.routers import user, course
from app.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="", tags=["users"])
app.include_router(course.router, prefix="", tags=["courses"])