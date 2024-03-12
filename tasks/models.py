from django.db import models

from tasks.enums.TaskStatuses import TaskStatuses


class Task(models.Model):
    """Модель задачи"""
    name = models.CharField(max_length=200, verbose_name='Название', db_index=True)
    description = models.TextField(max_length=10000, verbose_name='Описание')
    status = models.CharField(max_length=255, choices=TaskStatuses.choices())
