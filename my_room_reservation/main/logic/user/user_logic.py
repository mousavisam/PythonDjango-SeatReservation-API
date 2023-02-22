from ...model.user_entity import User


class UserLogic:

    def get_user_by_id(self, user_id: int) -> User:

        return User.objects.filter(id=user_id).first
    