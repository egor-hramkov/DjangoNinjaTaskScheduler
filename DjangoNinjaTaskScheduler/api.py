import logging

from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import AsyncJWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

from tasks.views.task_view import router as tasks_router
from users.views.user_view import router as user_router

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(pathname)s at line %(lineno)d | %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)

api.add_router("/tasks/", tasks_router, tags=["tasks"], auth=AsyncJWTAuth())
api.add_router("/users/", user_router, tags=["users"])
