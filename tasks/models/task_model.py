from django.contrib.auth.models import User
from django.db import models

from tasks.enums.task_statuses import TaskStatuses
from tasks.models.abstract_model import CreatedAndUpdatedAbstractModel


class Task(CreatedAndUpdatedAbstractModel):
    """Модель задачи"""
    name = models.CharField(max_length=200, verbose_name='Название', db_index=True)
    description = models.TextField(max_length=10000, verbose_name='Описание')
    status = models.CharField(max_length=255, choices=TaskStatuses.choices(), verbose_name='Статус')
    user = models.ForeignKey(
        User,
        verbose_name='Автор задачи',
        on_delete=models.CASCADE,
        related_name='tasks',
        null=False,
    )

    def __str__(self):
        return f"<{self.id}>: {self.name}. АВТОР: {self.user.username}"
