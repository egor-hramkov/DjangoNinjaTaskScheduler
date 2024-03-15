import logging

from django.core.exceptions import FieldError
from django.db.models import QuerySet
from ninja import Schema, Query

from users.domain.entities.abstract_user_ordering import AbstractUserOrderingEntity

logger = logging.getLogger(__name__)


class UserOrderingEntity(Schema, AbstractUserOrderingEntity):
    """Класс для поля сортировки пользователя"""
    ordering_field: str = Query(default=None, description="Any model field, for example: id or -id(for desc sorting)")

    def order(self, qs: QuerySet) -> QuerySet:
        """Выполняет сортировку в QuerySet"""
        try:
            qs = qs.order_by(self.ordering_field)
        except FieldError:
            logger.info(f"Передано несуществующее значение {self.ordering_field} для сортировки списка пользователя!")
        return qs
