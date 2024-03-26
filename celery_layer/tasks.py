import smtplib
from email.message import EmailMessage

from other_settings.redis_settings.redis_config import REDIS_CONFIG
from other_settings.smtp_settings.smtp_config import SMTP_CONFIG

from celery import Celery

redis_url = f'redis://{REDIS_CONFIG["REDIS_HOST"]}'
celery = Celery('tasks', broker=redis_url)


def get_email_template_dashboard(user_email: str, task_name: str):
    email = EmailMessage()
    email['Subject'] = f'Задача <{task_name}> переведена в статус выполнена!'
    email['From'] = SMTP_CONFIG["SMTP_USER"]
    email['To'] = user_email

    email.set_content(
        f"Статус вашей задачи <{task_name}> был изменён на выполнена!",
        subtype="plain",
        charset='utf-8'
    )
    return email


@celery.task
def send_email_about_done_task(user_email: str, task_name: str):
    email = get_email_template_dashboard(user_email, task_name)
    with smtplib.SMTP_SSL(SMTP_CONFIG["SMTP_HOST"], SMTP_CONFIG["SMTP_PORT"]) as server:
        server.login(SMTP_CONFIG["SMTP_USER"], SMTP_CONFIG["SMTP_PASSWORD"])
        server.send_message(email)

# celery -A celery_layer.tasks flower
# celery -A celery_layer.tasks worker --loglevel=INFO --pool=solo
