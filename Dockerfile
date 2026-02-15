FROM python:3.10-slim

WORKDIR /app

# Установка зависимостей системы (нужны для некоторых python пакетов)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Копирование проекта
COPY . .

# Команда запуска (Gunicorn)
CMD ["gunicorn", "mattress_prj.wsgi:application", "--bind", "0.0.0.0:8000"]