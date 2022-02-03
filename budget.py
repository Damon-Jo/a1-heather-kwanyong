from datetime import datetime
from transaction import Transaction



class Budget:
    """ A Budget Class"""

    def __init__(self, name: str, budget_limit: float, expenses: float,
                 remaining_balance: float, is_locked: bool, transaction_list: list) -> None:
        """
        Initialize attributes of Budget class.
        :param name: a string describing a category of the budget
        :param budget_limit: a float indicating the limit of the budget amount
        :param expenses: a float indicating the expense amount
        :param remaining_balance: a float indicating the remaining balance of the budget
        :param is_locked: true if the account is locked otherwise, false
        :param transaction_list: a list of transactions in this budget.
        """
        self._name = name
        self._budget_limit = budget_limit
        self._expenses = 0
        self._remaining_balance = remaining_balance
        self._transaction_list = []
        self._is_locked = is_locked

    # Accessors
    def get_remaining_balance(self) -> float:
        """
        Return remaining balance of the budget
        :return: a float
        """
        return self._remaining_balance

    def get_expenses(self) -> float:
        """
        Return expenses of the budget
        :return: a float
        """
        return self._expenses

    # remaining_balance = property(get_remaining_balance)

    def create_transaction(self, timestamp: datetime, dollar_amount: float, expense_location: str) -> Transaction:
        """
        Create a new transaction.
        :param timestamp: a datetime representing the time of the transaction
        :param dollar_amount: a float describing amount in dollar for the transaction
        :param expense_location: a string describing the location of expense
        """
        new_transaction = Transaction(timestamp, dollar_amount, expense_location)
        self._add_to_transaction(new_transaction)
        return new_transaction

    def _add_to_transaction(self, transaction: Transaction) -> None:
        """
        Add a transaction to the list.
        :param transaction: Transaction
        """
        self._transaction_list.apeend(transaction)


