from abc import ABC, abstractmethod


class AbstractTaskOrderingEntity(ABC):
    """Абстрактный Класс для поля сортировки задач"""
    ordering_field: str

    @abstractmethod
    def order(self, qs):
        """Выполняет сортировку"""
        raise NotImplementedError
