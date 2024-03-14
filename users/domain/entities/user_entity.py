from abc import ABC


class AbstractBaseUserEntity(ABC):
    """Абстракция базовой сущности пользователя"""
    username: str
    email: str
    first_name: str
    last_name: str


class AbstractUserInEntity(AbstractBaseUserEntity):
    """Абстрактная сущность запроса по пользователю"""
    password: str


class AbstractUserOutEntity(AbstractBaseUserEntity):
    """Абстрактная сущность ответа по пользователю"""
    id: int
