# Используем официальный образ Python
FROM python:3.9-slim

# Установка переменных окружения
ENV AUTHOR="Ваше имя"
ENV UUID="Любая произвольная строка"

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
