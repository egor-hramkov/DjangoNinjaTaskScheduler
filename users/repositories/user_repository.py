from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import aget_object_or_404

from users.domain.repository.abstract_user_repository import AbstractUserRepository
from users.exceptions.user_exceptions import UserDoesNotExistException
from users.entities.user_entity import UserInEntity, BaseUserEntity, UserOutEntity
from users.filters.user_filters import UserFilter
from users.filters.user_ordering import UserOrderingEntity


class UserRepository(AbstractUserRepository):
    """Репозиторий пользователей"""
    user_model: User = get_user_model()

    async def create(self, user_data: UserInEntity) -> UserOutEntity:
        """Создание пользователя"""
        hashed_password = make_password(user_data.password)
        user: User = await self.user_model.objects.acreate(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            username=user_data.username,
            password=hashed_password,
            email=user_data.email,
        )
        return UserOutEntity.model_validate(user, from_attributes=True)

    async def get(self, user_id: int) -> UserOutEntity:
        """Получение пользователя"""
        try:
            user = await self.user_model.objects.aget(pk=user_id)
        except User.DoesNotExist:
            raise UserDoesNotExistException
        return UserOutEntity.model_validate(user, from_attributes=True)

    async def update(self, user_id: int, user_data: BaseUserEntity) -> UserOutEntity:
        """Обновление пользователя"""
        user = await aget_object_or_404(User, pk=user_id)
        for attr, value in user_data.dict().items():
            setattr(user, attr, value)
        await user.asave()
        return UserOutEntity.model_validate(user, from_attributes=True)

    async def delete(self, user_id: int) -> None:
        """Удаление пользователя"""
        user = await aget_object_or_404(User, pk=user_id)
        await user.adelete()

    async def list(
            self,
            skip: int = 0,
            limit: int = 50,
            filters: UserFilter = None,
            ordering: UserOrderingEntity = None
    ) -> list[UserOutEntity]:
        """Получение списка пользователей"""
        qs = self.user_model.objects.all()
        if filters:
            qs = filters.filter(qs)
        if ordering:
            qs = ordering.order(qs)
        users = await sync_to_async(list)(qs[skip:limit])
        return [UserOutEntity.model_validate(user, from_attributes=True) for user in users]
