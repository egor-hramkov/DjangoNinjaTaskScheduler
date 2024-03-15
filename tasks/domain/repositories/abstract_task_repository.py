from abc import ABC, abstractmethod

from tasks.domain.entities.abstract_task_entity import (
    AbstractTaskInEntity,
    AbstractTaskOutEntity,
    AbstractTaskWithoutUserEntity
)
from tasks.domain.entities.abstract_task_filter import AbstractTaskFilter
from tasks.domain.entities.abstract_task_ordering import AbstractTaskOrderingEntity


class AbstractTaskRepository(ABC):
    """Абстрактный репозиторий задач"""

    @abstractmethod
    async def create(self, user_id: int, task_data: AbstractTaskInEntity) -> AbstractTaskOutEntity:
        """Создание задачи"""
        raise NotImplementedError

    @abstractmethod
    async def get(self, task_id: int) -> AbstractTaskOutEntity:
        """Получение задачи"""
        raise NotImplementedError

    @abstractmethod
    async def update(self, task_id: int, task_data: AbstractTaskInEntity) -> AbstractTaskOutEntity:
        """Обновление задачи"""
        raise NotImplementedError

    @abstractmethod
    async def delete(self, task_id: int) -> None:
        """Удаление задачи"""
        raise NotImplementedError

    @abstractmethod
    async def list(
            self,
            user_id: int,
            skip: int = 0,
            limit: int = 50,
            filters: AbstractTaskFilter = None,
            ordering: AbstractTaskOrderingEntity = None
    ) -> list[AbstractTaskWithoutUserEntity]:
        """Получение списка задач"""
        raise NotImplementedError
