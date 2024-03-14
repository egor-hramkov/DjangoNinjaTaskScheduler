from django.contrib.auth.models import User
from ninja import ModelSchema
from pydantic import EmailStr

from users.domain.entities.abstract_user_entity import AbstractUserInEntity, AbstractUserOutEntity, AbstractBaseUserEntity


class BaseUserEntity(ModelSchema, AbstractBaseUserEntity):
    """Базовая сущность пользователя"""
    email: EmailStr

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserInEntity(BaseUserEntity, AbstractUserInEntity):
    """Сущность для создания пользователя"""

    class Meta:
        model = User
        fields = ['password']


class UserOutEntity(BaseUserEntity, AbstractUserOutEntity):
    """Сущность для ответа пользователя"""

    class Meta:
        model = User
        fields = ['id']
