import os
from celery import Celery

broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
backend_url = os.environ.get("CELERY_RESULT_BACKEND", "mongodb://localhost:27017")

app = Celery("tasks", broker=broker_url, backend=backend_url)
