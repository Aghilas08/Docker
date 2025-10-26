# syntax=docker/dockerfile:1.7
# escape=\

FROM python:3.11-slim

WORKDIR /app

COPY . app/ /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000000

CMD ["python", "app.py"]
