from django.db import models


class AccountStatus(models.TextChoices):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
