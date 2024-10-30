# main.py
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, Base
from routes.project_route import router as project_router

app = FastAPI()

# Controlador de eventos de startup
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Incluir las rutas de proyectos
app.include_router(project_router, prefix="/projects", tags=["projects"])
