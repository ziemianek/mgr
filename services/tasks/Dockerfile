FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt      /app/requirements.txt
COPY ./services/tasks/app /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5050", "--reload"]
