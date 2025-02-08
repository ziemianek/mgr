FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

COPY ./services/tasks/app /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# https://docs.docker.com/reference/dockerfile/#entrypoint
ENTRYPOINT [ "uvicorn", "app.main:app" ]
