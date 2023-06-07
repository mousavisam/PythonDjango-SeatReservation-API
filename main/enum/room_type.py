from django.db import models


class RoomType (models.TextChoices):
    CINEMA = "CINEMA"
    RESTAURANT = "RESTAURANT"
    THEATER = "THEATER"
