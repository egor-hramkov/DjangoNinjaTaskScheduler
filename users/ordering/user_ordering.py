import logging

from django.core.exceptions import FieldError
from django.db.models import QuerySet
from ninja import Schema

logger = logging.getLogger(__name__)


class UserOrderingEntity(Schema):
    """Класс для поля сортировки пользователя"""
    ordering_field: str = None

    def order(self, qs: QuerySet) -> QuerySet:
        try:
            qs = qs.order_by(self.ordering_field)
        except FieldError:
            logger.info(f"Передано несуществующее значение {self.ordering_field} для сортировки списка пользователя!")
        return qs
