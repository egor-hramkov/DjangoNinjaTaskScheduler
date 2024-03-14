from typing import Optional

from ninja import FilterSchema


class UserFilter(FilterSchema):
    """Поля для фильтрации списка пользователей"""
    username: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

