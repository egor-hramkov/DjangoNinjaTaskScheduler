from tasks.domain.entities.task_entity import AbstractTaskSchema
from ninja import Schema


class TaskSchema(Schema, AbstractTaskSchema):
    """Сущность задачи"""
    ...

    def do(self):
        pass
