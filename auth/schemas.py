from ninja import Schema


class AuthSchema(Schema):
    username: str
    password: str


class JWTPairSchema(Schema):
    refresh: str
    access: str
