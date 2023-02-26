from ...model.transaction_entity import Transaction


class TransactionLogic:

    def insert_transaction(self, **kwargs):
        Transaction.objects.create(**kwargs)