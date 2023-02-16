from django.db import models


class TransactionStatus(models.TextChoices):
    FAILED = "FAILED"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"

