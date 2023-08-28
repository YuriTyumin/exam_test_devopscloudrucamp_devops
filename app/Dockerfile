# Используем официальный образ Python
FROM python:3.11-slim

# Установка переменных окружения
ENV AUTHOR="This could be your name"
ENV UUID="9259632c-7c5c-4e1b-b55f-1310f4e50c47"

# Создание и переключение на рабочую директорию
WORKDIR /app

# Копирование зависимостей и файла приложения
COPY requirements.txt .
COPY app.py .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8000
EXPOSE 8000

# Запуск приложения
CMD ["python", "app.py"]
