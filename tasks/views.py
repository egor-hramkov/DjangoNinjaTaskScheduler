from ninja import Router

router = Router()


class TaskSchema:
    """Сущность задачи"""
    ...


@router.post('/')
async def a():
    pass
