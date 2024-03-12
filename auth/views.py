from ninja import Router

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from auth.schemas import AuthSchema, JWTPairSchema

router = Router()


@router.post('/login', response=JWTPairSchema, auth=None)
def login(request, auth: AuthSchema):
    user = authenticate(**auth.dict())
    if user is not None:
        refresh = RefreshToken.for_user(user)
    # ToDo raise ошибки при не найденном пользователе
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
