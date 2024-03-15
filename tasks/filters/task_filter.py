from datetime import datetime
from typing import Optional

from django.db.models import QuerySet, Q
from ninja import FilterSchema, Query

from tasks.exceptions.task_filter_exceptions import TaskWrongConditionException, TaskWrongDateException


class TaskFilter(FilterSchema):
    """Поля для фильтрации списка задач"""
    created_at: Optional[str] = Query(default=None, example="lt__15.03.24-13:30")
    updated_at: Optional[str] = Query(default=None, example="gt__15.03.24-13:30")
    name: Optional[str] = None
    status: Optional[str] = None

    # user_id: Optional[int] = None

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
                created_conditions = {
                    'gt': Q(created_at__gt=datetime_object),
                    'gte': Q(created_at__gte=datetime_object),
                    'le': Q(created_at__le=datetime_object),
                    'lte': Q(created_at__lte=datetime_object),
                    'eq': Q(created_at__eq=datetime_object),
                    'neq': Q(created_at__neq=datetime_object),
                }
                q &= created_conditions[condition]

            if self.updated_at:
                condition, datetime_obj = self.updated_at.split('__')
                datetime_object = datetime.strptime(datetime_obj, '%d.%m.%y-%H:%M')
                updated_conditions = {
                    'gt': Q(updated_at__gt=datetime_object),
                    'gte': Q(updated_at__gte=datetime_object),
                    'le': Q(updated_at__le=datetime_object),
                    'lte': Q(updated_at__lte=datetime_object),
                    'eq': Q(updated_at__eq=datetime_object),
                    'neq': Q(updated_at__neq=datetime_object),
                }
                q &= updated_conditions[condition]
        except KeyError:
            raise TaskWrongConditionException
        except ValueError:
            raise TaskWrongDateException
        return q
