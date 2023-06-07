from django.core.validators import MinValueValidator
from django.db import models

from ..enum.reservation_status import ReservationStatus
from ..model.seat_entity import Seat
from ..model.user_entity import User


class Reservation(models.Model):
    reserver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="reservation")
    final_price = models.FloatField(validators=[MinValueValidator(0.1)])
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)
    seat_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="reservations")
    status = models.CharField(max_length=20, choices=ReservationStatus.choices)
    cancel_request_time = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
