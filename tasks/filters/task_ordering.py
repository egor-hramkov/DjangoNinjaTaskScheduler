import logging

from django.core.exceptions import FieldError
from django.db.models import QuerySet
from ninja import Schema, Query

from tasks.domain.entities.abstract_task_ordering import AbstractTaskOrderingEntity

logger = logging.getLogger(__name__)


class TaskOrderingEntity(Schema, AbstractTaskOrderingEntity):
    """Класс для поля сортировки задач"""
    ordering_field: str = Query(default=None, description="Any model field, for example: id or -id(for desc sorting)")

    def order(self, qs: QuerySet) -> QuerySet:
        """Выполняет сортировку в QuerySet"""
        if self.ordering_field is None:
            return qs
        try:
            qs = qs.order_by(self.ordering_field)
        except FieldError:
            logger.info(f"Передано несуществующее значение {self.ordering_field} для сортировки задач!")
        return qs
