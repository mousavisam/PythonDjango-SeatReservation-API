from django.core.validators import MinValueValidator
from django.db import models

from .reservation_entity import Reservation
from ..enum.transaction_status import TransactionStatus
from ..model.account_entity import Account


class Transaction(models.Model):
    seat_owner_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="transactions")
    reserver_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="transaction")
    status = models.CharField(max_length=20, choices=TransactionStatus.choices)
    amount = models.FloatField(validators=[MinValueValidator(0.1)])
    reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)


