from typing import Optional

from ninja import FilterSchema
from pydantic import EmailStr

from users.domain.entities.abstract_user_filter import AbstractUserFilter


class UserFilter(FilterSchema, AbstractUserFilter):
    """Поля для фильтрации списка пользователей"""
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
