from django.core.validators import MinValueValidator
from django.db import models

from .reservation_entity import Reservation
from ..enum.transaction_status import TransactionStatus, TransactionType
from ..model.account_entity import Account


class Transaction(models.Model):
    seat_owner_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="transactions", null=True,
                                           blank=True)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="transaction")
    status = models.CharField(max_length=60, choices=TransactionStatus.choices)
    amount = models.FloatField(validators=[MinValueValidator(0.1)])
    reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING, null=True, blank=True)
    type = models.CharField(max_length=30, choices=TransactionType.choices, null=True, blank=True)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)


