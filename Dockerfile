# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos si existe
COPY requirements.txt ./

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido del directorio actual al directorio de trabajo en el contenedor
COPY app/ .

# Instalar la biblioteca de cryptography
RUN pip install cryptography

# Ejecutar el script
CMD ["python3", "password_manager.py"]

