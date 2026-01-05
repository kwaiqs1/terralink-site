FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 👇 ВОТ ЭТОГО ТЕБЕ НЕ ХВАТАЕТ: копируем весь проект (manage.py тоже)
COPY . .

# (можно оставить start.sh внутри /app, но ты запускаешь /start.sh — ок)
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
