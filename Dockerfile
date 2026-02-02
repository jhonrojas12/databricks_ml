FROM python:3.10-slim

# Evita pyc y buffering raro
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiamos dependencias
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install pytest

# Copiamos el código
COPY utils ./utils
COPY tests ./tests

# Comando por defecto: correr tests
CMD ["pytest"]
