from enum import Enum


class TaskStatuses(Enum):
    """Enum статусов задачи"""
    created = "created"
    active = "active"
    done = "done"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def for_docs(cls):
        return ', '.join(i.name for i in cls)
