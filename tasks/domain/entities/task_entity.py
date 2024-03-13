from abc import ABC, abstractmethod


class AbstractTaskSchema(ABC):
    """Абстрактная сущность задачи"""
    ...

    @abstractmethod
    def do(self):
        raise NotImplementedError
