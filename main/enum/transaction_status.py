from django.db import models


class TransactionStatus(models.TextChoices):
    FAILED = "FAILED"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"


class TransactionType(models.TextChoices):
    REGISTER = "REGISTER"
    RESERVE = "RESERVE"
    CANCELED = "CANCELED"
    RESELL = "RESELL"
