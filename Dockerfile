# Usar una imagen oficial de Python como imagen base
FROM python:3.9

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requisitos y instalar las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . .

# Ejecutar migraciones y luego iniciar el servidor de Django
CMD ["sh", "-c", "python cargar_comics.py && \ 
    python manage.py collectstatic --noinput && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000"]