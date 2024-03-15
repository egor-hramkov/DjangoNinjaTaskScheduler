from tasks.domain.entities.task_entity import AbstractTaskSchema
from ninja import ModelSchema

from tasks.models import Task
from users.entities.user_entity import UserOutEntity


class TaskInEntity(ModelSchema, AbstractTaskSchema):
    """Сущность входных данных задачи"""

    class Meta:
        model = Task
        fields = ['name', 'description', 'status']


class TaskOutEntity(ModelSchema):
    """Сущность выходных данных задачи"""
    user: UserOutEntity

    class Meta:
        model = Task
        fields = '__all__'


class TaskWithoutUserEntity(ModelSchema):
    """Сущность выходных данных задачи"""

    class Meta:
        model = Task
        exclude = ['user']
