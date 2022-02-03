from abc import ABC


class User (ABC):
    """ User class."""
    # TODO: type of account_num
    # TODO: is account number a string or an int?
    def __init__(self, user_name: str, age: int, user_type: str, account_num,
                 bank_name: str, bank_balance: int, user_budget: int) -> None:
        """
        Initialize attributes of User class.
        :param user_name: a string
        :param age: a integer
        :param user_type: a string
        :param account_num: an integer
        :param bank_name: a string
        :param bank_balance: an integer
        :param user_budget: an integer
        """
        self._user_name = user_name
        self._age = age
        self._user_type = user_type
        self._account_num = account_num
        self._bank_name = bank_name
        self._bank_balance = bank_balance
        self._user_budget = user_budget


