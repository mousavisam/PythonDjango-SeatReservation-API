from django.db import models


class NotificationType(models.TextChoices):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
