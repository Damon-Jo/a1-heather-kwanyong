from datetime import datetime


class Transaction:
    """ A transaction class."""

    def __init__(self, timestamp: datetime, dollar_amount: float, expense_location: str) -> None:
        """
        Initialize attributes of Transaction class.
        :param timestamp: a datetime describing the time of transaction
        :param dollar_amount: a float describing the amount in dollar for the transaction
        :param expense_location: a string describing the location of expense
        """
        self._timestamp = timestamp
        self._dollar_amount = dollar_amount
        self._expense_location = expense_location

    # Accessors
    def get_timestamp(self) -> datetime:
        """
        Return timestamp of the transaction.
        :return: a datetime
        """
        return self._timestamp

    def get_dollar_amount(self) -> float:
        """
        Return dollar amount of the transaction.
        :return: a float
        """
        return self._dollar_amount

    def get_expense_location(self) -> str:
        """
        Return expense location of the transaction.
        :return: a string
        """
        return self._expense_location

    # Mutator
    def set_timestamp(self, timestamp: datetime) -> None:
        """
        Set value for timestamp.
        :param timestamp: a datetime
        """

    def set_dollar_amount(self, dollar_amount: float) -> None:
        """
        Set value for dollar amount.
        :param dollar_amount: a float
        """

    def set_expense_location(self, expense_location: str) -> None:
        """
        Set value for expense location.
        :param expense_location: a string
        """

    # Properties
    timestamp = property(get_timestamp, set_timestamp)
    dollar_amount = property(get_dollar_amount, set_dollar_amount)
    expense_location = property(get_expense_location, set_expense_location)