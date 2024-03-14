from abc import ABC, abstractmethod

from users.domain.entities.abstract_user_filter import AbstractUserFilter
from users.domain.entities.abstract_user_entity import AbstractUserInEntity, AbstractUserOutEntity
from users.domain.entities.abstract_user_ordering import AbstractUserOrderingEntity


class AbstractUserRepository(ABC):
    """Абстратный репозиторий пользователя"""

    @abstractmethod
    async def create(self, user_data: AbstractUserInEntity) -> AbstractUserOutEntity:
        """Создание пользователя"""
        raise NotImplementedError

    @abstractmethod
    async def get(self, user_id: int) -> AbstractUserOutEntity:
        """Получение пользователя"""
        raise NotImplementedError

    @abstractmethod
    async def update(self, user_id: int, user_data: AbstractUserInEntity) -> AbstractUserOutEntity:
        """Обновление пользователя"""
        raise NotImplementedError

    @abstractmethod
    async def delete(self, user_id: int) -> None:
        """Удаление пользователя"""
        raise NotImplementedError

    @abstractmethod
    async def list(
            self,
            skip: int = 0,
            limit: int = 50,
            filters: AbstractUserFilter = None,
            ordering: AbstractUserOrderingEntity = None
    ) -> list[AbstractUserOutEntity]:
        """Получение списка пользователей"""
        raise NotImplementedError
