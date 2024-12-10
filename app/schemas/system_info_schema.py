# schemas/system_info.py
from pydantic import BaseModel
from datetime import datetime

class ProjectCreate(BaseModel):
    host: str
    cpu_usage: float
    memory_usage: float
    disk_usage: str
    top_processes: str
    failed_services: str
    uptime: str
    network_info: str
    connections:str
    swap_usage: str
    error_logs: str
    timestamp: datetime

class ProjectResponse(ProjectCreate):
    id: int

    class Config:
        from_attributes = True