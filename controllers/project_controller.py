# controllers/project.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.project_model import Project
from schemas.project_schema import ProjectCreate, ProjectResponse

async def create_project(project_data: ProjectCreate, db: AsyncSession) -> ProjectResponse:
    project = Project(**project_data.dict())
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project

async def read_projects(db: AsyncSession) -> list[ProjectResponse]:
    result = await db.execute(select(Project))
    return result.scalars().all()

async def update_project_status(project_id: int, is_completed: bool, db: AsyncSession) -> ProjectResponse:
    project = await db.get(Project, project_id)
    project.is_completed = is_completed
    await db.commit()
    await db.refresh(project)
    return project

async def delete_project(project_id: int, db: AsyncSession) -> dict:
    project = await db.get(Project, project_id)
    if project:
        await db.delete(project)
        await db.commit()
        return {"message": "Project deleted successfully"}
    return {"message": "Project not found"}
