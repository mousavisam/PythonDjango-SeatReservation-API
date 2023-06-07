from django.core.validators import MinValueValidator
from django.db import models

from .reservation_entity import Reservation
from ..model.user_entity import User


class Resell(models.Model):
    reserver = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING)
    new_price = models.FloatField(validators=[MinValueValidator(0.1)])
    creation_time = models.DateTimeField(auto_now_add=True)
