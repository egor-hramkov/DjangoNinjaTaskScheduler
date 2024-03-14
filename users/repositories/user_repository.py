from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import aget_object_or_404

from users.exceptions.user_exceptions import UserDoesNotExistException
from users.entities.user_entity import UserInEntity, BaseUserEntity


class UserRepository:
    """Репозиторий пользователей"""
    user_model: User = get_user_model()

    async def create(self, user_data: UserInEntity):
        hashed_password = make_password(user_data.password)
        user = await self.user_model.objects.acreate(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            username=user_data.username,
            password=hashed_password,
            email=user_data.email,
        )
        return user

    async def get(self, user_id: int):
        """Получение пользователя"""
        try:
            user = await self.user_model.objects.aget(pk=user_id)
        except User.DoesNotExist:
            raise UserDoesNotExistException
        return user

    async def update(self, user_id: int, user_data: BaseUserEntity):
        """Обновление пользователя"""
        user = await aget_object_or_404(User, pk=user_id)
        for attr, value in user_data.dict().items():
            setattr(user, attr, value)
        await user.asave()
        return user

    async def delete(self, user_id: int):
        """Удаление пользователя"""
        user = await aget_object_or_404(User, pk=user_id)
        await user.adelete()

    async def list(self, skip: int = 0, limit: int = 50):
        """Получение списка пользователей"""
        users = await sync_to_async(list)(self.user_model.objects.all()[skip:limit])
        return users
