from ninja import Router
from ninja.params.functions import Query

from users.entities.user_entity import UserInEntity, UserOutEntity, BaseUserEntity
from users.services.user_service import UserService

router = Router()

user_service = UserService()


@router.post('/', response=UserOutEntity)
async def create(request, user_data: UserInEntity):
    """Создание пользователя"""
    user = await user_service.create(user_data)
    return user


@router.get('/{user_id}', response=UserOutEntity)
async def get(request, user_id: int):
    """Получение пользователя по айди"""
    user = await user_service.get(user_id)
    return user


@router.put('/{user_id}', response=UserOutEntity)
async def update(request, user_id: int, user_data: BaseUserEntity):
    """Обновление пользователя"""
    user = await user_service.update(user_id, user_data)
    return user


@router.delete('/{user_id}')
async def delete(request, user_id: int) -> dict:
    """Удаление пользователя"""
    await user_service.delete(user_id)
    return {"success": True}


@router.get('/', response=list[UserOutEntity])
async def list(
        request,
        skip: int = Query(ge=0, default=0),
        limit: int = Query(ge=0, default=50)
):
    """Получение списка пользователей"""
    users = await user_service.list(skip=skip, limit=limit)
    return users
