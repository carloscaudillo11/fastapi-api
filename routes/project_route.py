# routes/project_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from database import AsyncSessionLocal
from controllers.project_controller import (
    create_project,
    read_projects,
    update_project_status,
    delete_project
)
from schemas.project_schema import ProjectCreate, ProjectResponse

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Rutas
@router.post("/", response_model=ProjectResponse)
async def create_project_route(project: ProjectCreate, db: AsyncSession = Depends(get_db)):
    return await create_project(project, db)

@router.get("/", response_model=List[ProjectResponse])
async def read_projects_route(db: AsyncSession = Depends(get_db)):
    return await read_projects(db)

@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project_status_route(project_id: int, is_completed: bool, db: AsyncSession = Depends(get_db)):
    return await update_project_status(project_id, is_completed, db)

@router.delete("/{project_id}", response_model=dict)
async def delete_project_route(project_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_project(project_id, db)
