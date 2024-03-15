from abc import ABC


class AbstractBaseTaskEntity(ABC):
    """Абстрактная базовая сущност задачи"""
    name: str
    description: str
    status: str


class AbstractTaskInEntity(AbstractBaseTaskEntity):
    """Абстрактная Сущность входных данных задачи"""
    ...


class AbstractTaskOutEntity(AbstractBaseTaskEntity):
    """Абстрактная Сущность выходных данных задачи"""
    created_at: str
    updated_at: str
    user: dict


class AbstractTaskWithoutUserEntity(AbstractBaseTaskEntity):
    """Абстрактная Сущность выходных данных задачи без пользователя"""
    created_at: str
    updated_at: str
