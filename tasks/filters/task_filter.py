import logging
from datetime import datetime
from typing import Optional

from django.db.models import Q
from ninja import FilterSchema, Query

from tasks.domain.entities.abstract_task_filter import AbstractTaskFilter
from tasks.exceptions.task_filter_exceptions import TaskWrongConditionException, TaskWrongDateException

logger = logging.getLogger(__name__)


class TaskFilter(FilterSchema, AbstractTaskFilter):
    """Поля для фильтрации списка задач"""
    created_at: Optional[str] = Query(
        default=None,
        description="Фильтрация по времени создания, поддерживает gt,gte,lte,lt,eq. For example: lt__15.03.24-13:30",
    )
    updated_at: Optional[str] = Query(
        default=None,
        description="Фильтрация по времени создания, поддерживает gt,gte,lte,lt,eq. For example: lt__15.03.24-13:30",
    )
    name: Optional[str] = None
    status: Optional[str] = Query(
        default=None,
        description="Allowed statuses: 'created', 'active', 'done'",
    )

    @staticmethod
    def get_created_at_conditions(datetime_object: datetime) -> dict:
        return {
            'gt': Q(created_at__gt=datetime_object),
            'gte': Q(created_at__gte=datetime_object),
            'lt': Q(created_at__lt=datetime_object),
            'lte': Q(created_at__lte=datetime_object),
            'eq': Q(created_at__eq=datetime_object),
            'neq': Q(created_at__neq=datetime_object),
        }

    @staticmethod
    def get_updated_at_conditions(datetime_object: datetime) -> dict:
        return {
            'gt': Q(updated_at__gt=datetime_object),
            'gte': Q(updated_at__gte=datetime_object),
            'lt': Q(updated_at__lt=datetime_object),
            'lte': Q(updated_at__lte=datetime_object),
            'eq': Q(updated_at__eq=datetime_object),
            'neq': Q(updated_at__neq=datetime_object),
        }

    def custom_expression(self) -> Q:
        """Кастомное выражение для фильтрации задач"""
        q = Q()

        if self.name:
            q &= Q(name__icontains=self.name)

        if self.status:
            q &= Q(status=self.status)

        try:
            if self.created_at:
                condition, datetime_obj = self.created_at.split('__')
                datetime_object = datetime.strptime(datetime_obj, '%d.%m.%y-%H:%M')
                created_conditions = self.get_created_at_conditions(datetime_object)
                q &= created_conditions[condition]

            if self.updated_at:
                condition, datetime_obj = self.updated_at.split('__')
                datetime_object = datetime.strptime(datetime_obj, '%d.%m.%y-%H:%M')
                updated_conditions = self.get_updated_at_conditions(datetime_object)
                q &= updated_conditions[condition]
        except KeyError:
            logger.error(f"Передан неверный ключ для фильтрации по времени"
                         f"{self.created_at=}, {self.updated_at=}, {condition=}, {datetime_object=} ")
            raise TaskWrongConditionException
        except ValueError:
            logger.error(f"Передана неверная дата для фильтрации задач {self.created_at=}, {self.updated_at=}")
            raise TaskWrongDateException
        return q
