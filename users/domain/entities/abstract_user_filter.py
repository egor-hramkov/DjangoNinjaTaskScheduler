from abc import ABC


class AbstractUserFilter(ABC):
    """Абстракция полей для фильтрации списка пользователей"""
    username: str
    email: str
    first_name: str
    last_name: str
