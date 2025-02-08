FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

COPY ./services/tasks/app /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# TODO: Should use ENTRYPOINT, and pass flags as CMD during start
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5050", "--reload"]
ENTRYPOINT [ "uvicorn", "app.main:app" ]
