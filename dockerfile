# Usar una imagen base de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar las dependencias y netcat
RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar el resto del código de la aplicación
COPY . .

# Dar permisos de ejecución al script de inicio
RUN chmod +x start.sh

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# Usar el script de inicio como punto de entrada
CMD ["./start.sh"]