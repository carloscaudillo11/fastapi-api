# models/models.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    student_name = Column(String)
    student_id = Column(String)
    advisor_name = Column(String)
    career = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)
