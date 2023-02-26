from decimal import Decimal

from django.db.models import QuerySet

from ..account.account_logic import AccountLogic
from ..transaction.transaction_logic import TransactionLogic
from ...enum.account_status import AccountStatus, AccountType
from ...enum.transaction_status import TransactionStatus, TransactionType
from ...model.user_entity import User


class RegisterLogic:
    def __init__(self) -> None:
        super().__init__()
        self.account_logic = AccountLogic()
        self.transaction_logic = TransactionLogic()
    def get_all_users(self) -> QuerySet:
        return User.objects.all()

    def insert_user(self, **kwargs) -> int:
        password = kwargs.pop('password')
        user = User.objects.create(**kwargs)
        user.set_password(password)
        user.save()
        return user

    def register_new_user(self, **kwargs):
        base_balance = 2000
        user = self.insert_user(**kwargs)
        user_account = self.account_logic.insert_account(user=user, balance=0, status=AccountStatus.ACTIVE,
                                                         type=AccountType.USER)
        system_account = self.account_logic.get_account_by_type(account_type=AccountType.SYSTEM)

        self.account_logic.update_account_balance(system_account, Decimal(-base_balance))
        self.account_logic.update_account_balance(user_account[0], Decimal(base_balance))
        self.transaction_logic.insert_transaction(account=system_account, amount=-base_balance,
                                                  status=TransactionStatus.SUCCESS, type=TransactionType.REGISTER,
                                                  description="update new user balance")
        self.transaction_logic.insert_transaction(account=user_account[0], amount=base_balance,
                                                  status=TransactionStatus.SUCCESS, type=TransactionType.REGISTER,
                                                  description="update new user balance")
