from app.libs.execute_command import execute_ssh_command
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.schemas.system_info_schema import ProjectResponse
from app.libs.save_info import save_info, parse_usage

async def get_system_info(
    host: str,
    username: str,
    password: str,
    port: int,
    commands: dict,
    db: AsyncSession,
) -> ProjectResponse:
    async def safe_execute(command_key):
        try:
            return execute_ssh_command(
                host, username, password, commands[command_key], port
            ).strip()
        except Exception as cmd_error:
            # Aquí registramos el error específico para depuración
            print(f"Error ejecutando el comando {command_key}: {str(cmd_error)}")
            return f"Error ejecutando {command_key}: {str(cmd_error)}"

    try:
        results = {key: await safe_execute(key) for key in commands}
        
        disk_list = [
            {
                "filesystem": parts[0],
                "size": parts[1],
                "used": parts[2],
                "available": parts[3],
                "usage": parts[4],
                "mount_point": parts[5],
            }
            for line in results["disks"].splitlines()
            if (parts := line.split())
            and not any(skip in parts[0] for skip in ["tmpfs", "overlay", "loop"])
        ]
        results["important_disks"] = sorted(
            disk_list, key=lambda d: parse_usage(d["usage"]), reverse=True
        )[:3]

        system_info = await save_info(results, host, db)
        return system_info

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener y guardar información del sistema: {str(e)}",
        )
