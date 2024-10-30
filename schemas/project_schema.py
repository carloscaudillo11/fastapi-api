# schemas/project.py
from pydantic import BaseModel

class ProjectCreate(BaseModel):
    title: str
    student_name: str
    student_id: str
    advisor_name: str
    career: str
    description: str
    is_completed: bool = False

class ProjectResponse(ProjectCreate):
    id: int

    class Config:
        orm_mode = True
