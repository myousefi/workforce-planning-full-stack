# Dockerfile
FROM python:3.11-slim-bullseye

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY . .

CMD ["python", "app/tasks/celery_worker.py"]
