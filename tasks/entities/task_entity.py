from ninja import ModelSchema, Query

from tasks.domain.entities.abstract_task_entity import (
    AbstractTaskWithoutUserEntity,
    AbstractTaskOutEntity,
    AbstractTaskInEntity, AbstractBaseTaskEntity
)
from tasks.enums.task_statuses import TaskStatuses
from tasks.models import Task
from users.entities.user_entity import UserOutEntity


class BaseTaskEntity(ModelSchema, AbstractBaseTaskEntity):
    """Базовая сущность задачи"""

    status: str = Query(
        default=None,
        example=f"{TaskStatuses.for_docs()}",
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status']


class TaskInEntity(BaseTaskEntity, AbstractTaskInEntity):
    """Сущность входных данных задачи"""
    ...


class TaskOutEntity(ModelSchema, AbstractTaskOutEntity):
    """Сущность выходных данных задачи"""
    user: UserOutEntity

    class Meta:
        model = Task
        fields = '__all__'


class TaskWithoutUserEntity(ModelSchema, AbstractTaskWithoutUserEntity):
    """Сущность выходных данных задачи"""

    class Meta:
        model = Task
        exclude = ['user']
