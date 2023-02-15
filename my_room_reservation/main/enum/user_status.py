from django.db import models


class UserType(models.TextChoices):
    ADMIN = "ADMIN"
    PRODUCT_OWNER = "PRODUCT_OWNER"
    REGULAR_USER = "REGULAR_USER"
