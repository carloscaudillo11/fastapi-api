from app.libs.execute_command import execute_ssh_command
import json
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.models.system_info_model import SystemInfo
from app.schemas.system_info_schema import ProjectResponse
import re

def safe_json_serialize(data):
    try:
        return json.dumps(data)
    except Exception as e:
        return f"Error al serializar datos: {str(e)}"


def parse_usage(usage):
    """Extrae el valor numérico del porcentaje de uso, si es válido."""
    match = re.match(r"(\d+)", usage.strip("%"))
    if match:
        return int(match.group(1))
    return 0


async def save_info(results: dict, host: str, db: AsyncSession):
    try:
        def safe_float(value, default=0.0):
            try:
                return float(value.strip("%"))
            except (ValueError, AttributeError):
                return default

        system_info = SystemInfo(
            host=host,
            cpu_usage=safe_float(results.get("cpu", "0")),
            memory_usage=safe_float(results.get("memory", "0")),
            disk_usage=json.dumps(results.get("important_disks", [])),
            top_processes=json.dumps(results.get("top_processes", "").splitlines()),
            failed_services=json.dumps(results.get("failed_services", "").splitlines()),
            uptime=results.get("uptime", "N/A"),
            network_info=json.dumps(results.get("network", "").splitlines()),
            connections=json.dumps(results.get("connections", "").splitlines()),
            swap_usage=results.get("swap", "0"),
            error_logs=json.dumps(results.get("errors", "").splitlines()),
        )

        db.add(system_info)
        await db.commit()
        await db.refresh(system_info)

        return system_info

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al guardar información del sistema en la base de datos: {str(e)}",
        )