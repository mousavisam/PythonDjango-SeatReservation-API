from django.db import models


class UserType(models.TextChoices):
    ADMIN = "ADMIN"
    REGULAR_USER = "REGULAR_USER"
    BUSINESS_OWNER = "BUSINESS_OWNER"
