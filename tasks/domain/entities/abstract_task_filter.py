from abc import ABC


class AbstractTaskFilter(ABC):
    """Абстракция полей для фильтрации списка пользователей"""
    created_at: str
    updated_at: str
    name: str
    status: str
