
import time
from celery import Celery

celery_app = Celery(
    "tasks",
    broker="sqla+sqlite:///celery_queue.db",
    backend="db+sqlite:///celery_results.db"
)

celery_app.conf.task_track_started = True


@celery_app.task
def send_welcome_email(email):
    time.sleep(10)

    return {
        "email": email,
        "message": "Письмо успешно обработано"
    }