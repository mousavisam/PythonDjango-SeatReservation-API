from decimal import Decimal

from ...enum.account_status import AccountType
from ...model.account_entity import Account
from ...model.user_entity import User


class AccountLogic:

    def insert_account(self, **kwargs) -> Account:
        return Account.objects.get_or_create(**kwargs)

    def update_account_balance(self, account: Account, balance: Decimal) -> None:
        account.balance += balance
        account.save()

    def get_account_by_type(self, account_type: AccountType) -> Account:
        return Account.objects.filter(type=account_type).first()

    def get_account_by_user(self, user: User) -> Account:
        return Account.objects.filter(user=user).first()
