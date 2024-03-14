from abc import ABC, abstractmethod


class AbstractUserOrderingEntity(ABC):
    """Класс для поля сортировки пользователя"""
    ordering_field: str = None

    @abstractmethod
    def order(self, qs):
        """Выполняет сортировку"""
        raise NotImplementedError
