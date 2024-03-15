from tasks.entities.task_entity import TaskInEntity, TaskOutEntity, TaskWithoutUserEntity
from tasks.filters.task_filter import TaskFilter
from tasks.filters.task_ordering import TaskOrderingEntity
from tasks.repositories.task_repository import TaskRepository


class TaskService:
    """Сервис пользователей"""
    _repository = TaskRepository()

    async def create(self, user_id: int, task_data: TaskInEntity) -> TaskOutEntity:
        """Создание пользователя"""
        task = await self._repository.create(user_id, task_data)
        return task

    async def get(self, task_id: int) -> TaskOutEntity:
        """Получение пользователя"""
        task = await self._repository.get(task_id)
        return task

    async def update(self, task_id: int, task_data: TaskInEntity) -> TaskOutEntity:
        """Обновление пользователя"""
        user = await self._repository.update(task_id, task_data)
        return user

    async def delete(self, task_id: int):
        """Удаление пользователя"""
        await self._repository.delete(task_id)

    async def list(
            self,
            user_id: int,
            skip: int = 0,
            limit: int = 50,
            filters: TaskFilter = None,
            ordering: TaskOrderingEntity = None
    ) -> list[TaskWithoutUserEntity]:
        """Получение списка пользователя"""
        tasks = await self._repository.list(user_id=user_id, skip=skip, limit=limit, filters=filters, ordering=ordering)
        return tasks
