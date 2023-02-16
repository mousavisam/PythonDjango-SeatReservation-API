from django.core.validators import MinValueValidator
from django.db import models

from ..enum.seat_enum import Position, Status
from ..model.room_entity import Room


class Seat(models.Model):
    price = models.PositiveIntegerField(validators=[MinValueValidator(0.1)])
    position = models.CharField(max_length=12, choices=Position.choices)
    status = models.CharField(max_length=12, choices=Status.choices)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
