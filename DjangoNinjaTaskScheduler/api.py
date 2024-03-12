from ninja import NinjaAPI
from ninja_jwt.authentication import JWTAuth

from auth.jwt_auth_model import JWTAuthRequired
from auth.views import router as auth_router
from tasks.views import router as tasks_router

api = NinjaAPI()
api.add_router("/tasks/", tasks_router, tags=["tasks"], auth=JWTAuth())
api.add_router("/auth/", auth_router, tags=["auth"])
