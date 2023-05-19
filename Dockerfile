# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación en el contenedor
COPY . /app

# Instala las dependencias del proyecto en el entorno virtual
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP app
ENV FLASK_RUN_HOST 0.0.0.0


# Expone el puerto en el que se ejecuta la aplicación Flask
EXPOSE 5000

# Ejecuta la aplicación Flask cuando se inicie el contenedor
CMD ["python", "./src/app.py"]
