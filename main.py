# main.py
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, Base
from app.routes.system_monitor_route import router as system_monitor_router

app = FastAPI()

# Controlador de eventos de startup
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Incluir las rutas de proyectos
app.include_router(system_monitor_router, prefix="/system_monitor", tags=["system_monitor"])
