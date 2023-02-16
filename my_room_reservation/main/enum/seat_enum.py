from django.db import models


class Position(models.TextChoices):
    FIRST_ROW = "FIRST_ROW"
    LAST_ROW = "LAST_ROW"
    MIDDLE_ROWS = "MIDDLE_ROWS"


class Status(models.TextChoices):
    RESERVED = "RESERVED"
    UNRESERVED = "UNRESERVED"


