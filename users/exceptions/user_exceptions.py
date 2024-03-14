from ninja_extra import status
from ninja_extra.exceptions import APIException


class UserDoesNotExistException(APIException):
    """Ошибка пользователь не существует"""
    status_code = status.HTTP_400_BAD_REQUEST
    message = 'Пользователь не найден'
