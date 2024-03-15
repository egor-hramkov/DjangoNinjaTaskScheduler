from asgiref.sync import sync_to_async
from django.shortcuts import aget_object_or_404

from tasks.entities.task_entity import TaskInEntity, TaskOutEntity, TaskWithoutUserEntity
from tasks.filters.task_filter import TaskFilter
from tasks.models import Task


class TaskRepository:
    """Репозиторий Задач"""

    async def create(self, user_id: int, task_data: TaskInEntity) -> TaskOutEntity:
        """Создание задачи"""
        task = await Task.objects.acreate(
            **task_data.dict(),
            user_id=user_id
        )
        return await sync_to_async(TaskOutEntity.model_validate)(task, from_attributes=True)

    async def get(self, task_id: int) -> TaskOutEntity:
        """Получение задачи"""
        task = await aget_object_or_404(Task, pk=task_id)
        return await sync_to_async(TaskOutEntity.model_validate)(task, from_attributes=True)

    async def update(self, task_id: int, task_data: TaskInEntity) -> TaskOutEntity:
        """Обновление задачи"""
        task = await aget_object_or_404(Task, pk=task_id)
        for attr, value in task_data.dict().items():
            setattr(task, attr, value)
        await task.asave()
        return await sync_to_async(TaskOutEntity.model_validate)(task, from_attributes=True)

    async def delete(self, task_id: int) -> None:
        """Удаление задачи"""
        task = await aget_object_or_404(Task, pk=task_id)
        await task.adelete()

    async def list(
            self,
            user_id: int,
            skip: int = 0,
            limit: int = 50,
            filters: TaskFilter = None,
            # ordering: UserOrderingEntity = None
    ) -> list[TaskWithoutUserEntity]:
        """Получение списка задач"""
        qs = Task.objects.filter(user_id=user_id)
        if filters:
            qs = filters.filter(qs)
        # if ordering:
        #     qs = ordering.order(qs)
        tasks = await sync_to_async(list)(qs[skip:limit])
        return [await sync_to_async(TaskWithoutUserEntity.model_validate)(task, from_attributes=True) for task in tasks]
