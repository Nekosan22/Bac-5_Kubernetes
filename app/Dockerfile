FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Utilisation de Gunicorn pour lancer l'application en production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]