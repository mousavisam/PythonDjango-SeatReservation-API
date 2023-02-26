from django.db import models

from .user_entity import User
from ..enum.account_status import AccountStatus, AccountType


class Account(models.Model):
    balance = models.DecimalField(max_digits=12, decimal_places=3)
    creation_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, related_name="account")
    status = models.CharField(max_length=20, choices=AccountStatus.choices)
    type = models.CharField(max_length=20, choices=AccountType.choices)