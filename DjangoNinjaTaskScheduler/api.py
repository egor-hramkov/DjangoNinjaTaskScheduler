from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

from tasks.views.task_view import router as tasks_router
from users.views.user_view import router as user_router

api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)

api.add_router("/tasks/", tasks_router, tags=["tasks"], auth=JWTAuth())
api.add_router("/users/", user_router, tags=["users"])
