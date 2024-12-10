from fastapi import APIRouter
from app.controllers.system_monitor_controller import get_system_info
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from database import AsyncSessionLocal
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.system_info_schema import ProjectResponse

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

"""
@router.get("/info/ubuntu")
def server_info_ubuntu(
    host: str, username: str, password: str
):
    return get_server_info(host, username, password)
"""

@router.get("/info/ubuntu", response_model=ProjectResponse)
async def server_info_ubuntu(
    host: str, username: str, password: str, port: int = 55220, db: AsyncSession = Depends(get_db)
):
    commands = {
        "cpu": "top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}'",
        "memory": "free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'",
        "disks": "df -h | awk 'NR>1 {print $1, $2, $3, $4, $5, $6}'",
        "top_processes": "ps aux --sort=-%cpu | head -n 5",
        "failed_services": "systemctl --failed --no-pager | grep -E '(failed|inactive)'",
        "uptime": "uptime -p",
        "network": "ip -s link",
        "connections": "ss -tuln",
        "swap": "free -m | grep Swap | awk '{print $3 \"/\" $2}'",
        "errors": "journalctl -p 3 -b --lines=50",
    }
    return await get_system_info(host, username, password, port, commands, db)


@router.get("/info/redhat", response_model=ProjectResponse)
async def server_info_redhat(
    host: str, username: str, password: str,  port: int = 55220, db: AsyncSession = Depends(get_db)
):
    commands = {
        "cpu": "top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}'",
        "memory": "free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'",
        "disks": "df -h --output=source,size,used,avail,pcent,target | tail -n +2",
        "top_processes": "ps aux --sort=-%cpu | head -n 5",
        "failed_services": "systemctl --failed --no-pager",
        "uptime": "uptime -p",
        "network": "ip -s link",
        "connections": "ss -tuln",
        "swap": "free -m | grep Swap | awk '{print $3 \"/\" $2}'",
        "errors": "journalctl -p 3 -b --lines=50",
    }
    return await get_system_info(host, username, password, port, commands, db)
