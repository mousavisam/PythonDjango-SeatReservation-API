import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet

from ...logic.user.user_logic import UserLogic
from ...model.comment_entity import Comment
from ...model.user_entity import User


class CommentLogic:

    def __init__(self):
        super().__init__()
        self.user_logic = UserLogic()

    def save_comments(self, receiver_username: str, sender: User, message: str, parent: int = None):
        receiver_user = self.user_logic.get_user_by_username(receiver_username)
        if receiver_user:
            if parent:
                Comment.objects.create(sender=sender, receiver=receiver_user, message=message,
                                       creation_time=datetime.datetime.now(), parent_id=parent)
            else:
                comment = Comment(sender=sender, receiver=receiver_user, message=message,
                                  creation_time=datetime.datetime.now())
                comment.parent_id = Comment.objects.count() + 1
                comment.save()

        else:
            raise ObjectDoesNotExist

    def get_comments_by_sender(self, sender: User) -> QuerySet:
        return Comment.objects.filter(sender=sender)