from ...model.user_entity import User
from django.db.models import QuerySet


class RegisterLogic:

    def __init__(self) -> None:
        super().__init__()

    def get_all_users(self) -> QuerySet:
        return User.objects.all()

    def insert_user(self, **kwargs) -> int:
        password = kwargs.pop('password')
        user = User.objects.create(**kwargs)
        user.set_password(password)
        user.save()
        return user.id
