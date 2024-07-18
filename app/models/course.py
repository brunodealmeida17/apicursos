from sqlalchemy import Integer, String, Float, Boolean, Column, Text
from app.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, max_length=150, index=True)
    description = Column(Text)
    price = Column(Float)
    active = Column(Boolean, nullable=True, default=True)
