from ninja_extra import NinjaExtraAPI

from auth.jwt_auth_model import JWTAuthRequired
from auth.views import router as auth_router
from tasks.views import router as tasks_router

api = NinjaExtraAPI()
api.add_router("/tasks/", tasks_router, tags=["tasks"], auth=JWTAuthRequired)
api.add_router("/auth/", auth_router, tags=["auth"])
