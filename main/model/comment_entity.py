from django.db import models

from ..model.user_entity import User


class Comment(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comment')
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING,
                               related_name='parent_comment')
    message = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)