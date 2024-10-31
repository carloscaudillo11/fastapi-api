#!/bin/bash

# Esperar a que la base de datos esté disponible
echo "Esperando que la base de datos esté disponible..."
while ! nc -z db 5432; do   
  sleep 1 # Espera un segundo antes de verificar de nuevo
done

# Inicializar Alembic si no ha sido inicializado
if [ ! -d alembic ]; then
  echo "Inicializando Alembic..."
  alembic init alembic
fi

# Crear una migración inicial si no existe
if [ ! -f alembic/versions/initial_migration.py ]; then
  echo "Creando la migración inicial..."
  alembic revision --autogenerate -m "initial migration"
fi

# Ejecutar las migraciones
echo "Ejecutando migraciones..."
alembic upgrade head

# Iniciar la API
echo "Iniciando la API..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
