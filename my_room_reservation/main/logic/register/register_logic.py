from ...model.user_entity import User


class RegisterLogic:

    def get_all_users(self):
        return User.objects.all()
