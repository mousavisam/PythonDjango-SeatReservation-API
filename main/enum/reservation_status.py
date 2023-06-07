from django.db import models


class ReservationStatus(models.TextChoices):
    REQUESTED = "REQUESTED"
    CANCELED = "CANCELED"
    RESELL = "RESELL"
    SUCCESS = "SUCCESS"
