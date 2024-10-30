import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Obtener la URL de la base de datos desde la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/residencias")

# Crear el motor asíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear una sesión local asíncrona
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Crear la base declarativa
Base = declarative_base()
