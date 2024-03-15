from ninja_extra import status
from ninja_extra.exceptions import APIException


class TaskWrongConditionException(APIException):
    """Ошибка неверный ключ для фильтрации"""
    status_code = status.HTTP_400_BAD_REQUEST
    message = 'Передан неверный ключ для фильтрации'


class TaskWrongDateException(APIException):
    """Ошибка неверная дата для фильтрации"""
    status_code = status.HTTP_400_BAD_REQUEST
    message = 'Передана неверная дата для фильтрации'
