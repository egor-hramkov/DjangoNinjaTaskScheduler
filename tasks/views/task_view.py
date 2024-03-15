from ninja import Router
from ninja.params.functions import Query

from tasks.entities.task_entity import TaskInEntity, TaskOutEntity, TaskWithoutUserEntity
from tasks.filters.task_filter import TaskFilter
from tasks.services.task_service import TaskService

router = Router()

task_service = TaskService()


@router.post('/', response=TaskOutEntity)
async def create(request, task_data: TaskInEntity):
    """Создание задачи"""
    user = request.user
    task: TaskOutEntity = await task_service.create(user.id, task_data)
    return task


@router.get('/{task_id}', response=TaskOutEntity)
async def get(request, task_id: int):
    """Получение пользователя по айди"""
    task = await task_service.get(task_id)
    return task


@router.put('/{task_id}', response=TaskOutEntity)
async def update(request, task_id: int, task_data: TaskInEntity):
    """Обновление пользователя"""
    user = await task_service.update(task_id, task_data)
    return user


@router.delete('/{task_id}')
async def delete(request, task_id: int) -> dict:
    """Удаление пользователя"""
    await task_service.delete(task_id)
    return {"success": True}


@router.get('/', response=list[TaskWithoutUserEntity])
async def list(
        request,
        skip: int = Query(ge=0, default=0),
        limit: int = Query(ge=0, default=50),
        filters: TaskFilter = Query(default=None),
        # ordering: int = 1,
):
    """Получение списка пользователей"""
    user_id = request.user.id
    tasks = await task_service.list(user_id=user_id, skip=skip, limit=limit, filters=filters)
    return tasks
