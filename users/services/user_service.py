from users.entities.user_entity import UserInEntity, BaseUserEntity
from users.filters.user_filters import UserFilter
from users.filters.user_ordering import UserOrderingEntity
from users.repositories.user_repository import UserRepository


class UserService:
    """Сервис пользователей"""
    _repository = UserRepository()

    async def create(self, user_data: UserInEntity):
        """Создание пользователя"""
        user = await self._repository.create(user_data)
        return user

    async def get(self, user_id: int):
        """Получение пользователя"""
        user = await self._repository.get(user_id)
        return user

    async def update(self, user_id: int, user_data: BaseUserEntity):
        """Обновление пользователя"""
        user = await self._repository.update(user_id, user_data)
        return user

    async def delete(self, user_id: int):
        """Удаление пользователя"""
        await self._repository.delete(user_id)

    async def list(
            self,
            skip: int = 0,
            limit: int = 50,
            filters: UserFilter = None,
            ordering: UserOrderingEntity = None
    ):
        """Получение списка пользователя"""
        users = await self._repository.list(skip=skip, limit=limit, filters=filters, ordering=ordering)
        return users
