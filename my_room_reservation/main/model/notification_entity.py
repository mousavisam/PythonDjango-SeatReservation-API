from django.db import models

from ..enum.notification_type import NotificationType


class Notification(models.Model):
    message = models.TextField()
    type = models.CharField(max_length=60, choices=NotificationType.choices)
    is_read = models.BooleanField(default=False)
    creation_time = models.DateTimeField(auto_now_add=True)
