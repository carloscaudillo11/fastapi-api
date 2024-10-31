#!/bin/bash

# Esperar a que la base de datos esté disponible
echo "Esperando que la base de datos esté disponible..."
while ! nc -z db 5432; do   
  sleep 1 # Espera un segundo antes de verificar de nuevo
done

# Verificar si Alembic ya está inicializado (opcional si solo deseas inicializar una vez)
if [ ! -d alembic ]; then
  echo "Inicializando Alembic..."
  alembic init alembic
fi

# Crear una migración inicial solo si no existe
if [ ! "$(ls -A alembic/versions)" ]; then
  echo "Creando la migración inicial..."
  alembic revision --autogenerate -m "initial migration"
fi

# Ejecutar las migraciones
echo "Ejecutando migraciones..."
alembic upgrade head

# Iniciar la API
echo "Iniciando la API..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
