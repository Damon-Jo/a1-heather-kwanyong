from datetime import datetime
import transaction


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
        self._expenses = expenses
        self._remaining_balance = remaining_balance
        self._transaction_list = transaction_list
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

    def create_transaction(self, timestamp: datetime, dollar_amount: float, expense_location: str) -> None:
        """
        Create a new transaction.
        :param timestamp: a datetime representing the time of the transaction
        :param dollar_amount: a float describing amount in dollar for the transaction
        :param expense_location: a string describing the location of expense
        """
