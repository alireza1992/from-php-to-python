from celery import Celery

celery = Celery(
    "celery",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["infrastructure.celery.tasks"],
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
)