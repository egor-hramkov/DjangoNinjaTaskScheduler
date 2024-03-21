from django.db.models.signals import pre_save
from django.dispatch import receiver

from celery_layer.tasks import send_email_about_done_task
from tasks.enums.task_statuses import TaskStatuses
from tasks.models import Task


@receiver(pre_save, sender=Task)
def status_done_signal(sender, instance: Task, **kwargs):
    if instance.id is not None:
        instance_before: Task = sender.objects.get(pk=instance.pk)
        user = instance.user
        if instance.status == TaskStatuses.done.value and instance_before.status != instance.status:
            send_email_about_done_task.delay(user_email=user.email, task_name=instance.name)
