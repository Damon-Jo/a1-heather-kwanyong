from abc import ABC

from bank_account import BankAccount


class User (ABC):
    """ User class."""
    # TODO: type of account_num
    # TODO: is account number a string or an int? string
    def __init__(self, user_name: str, age: int, user_type: str,
                 warning, is_lockable, lock_limit) -> None:

    #def __init__(self, user_name: str, age: int, user_type: str, account_num,
    #             bank_name: str, bank_balance: int, user_budget: int) -> None:

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

        self._percentage_warning = warning
        self._is_lockable = is_lockable
        self._lock_limit = lock_limit
        self._locked_budgets = 0


        # self._account_num = account_num
        # self._bank_name = bank_name
        # self._bank_balance = bank_balance
        # self._user_budget = user_budget



        self._bank = self._validate_bank_details()

    def _validate_bank_details(self):
        while True:
            try:
                bank_details = self.input_bank_details()
            except ValueError:
                print("Amount would put balance below 0.")
            else:
                break
        return bank_details

    @staticmethod
    def input_bank_details():
        """
        Input the user for details and creates a bank account object with the details.
        :return: the newly created bank account
        """
        while True:
            bank_number = ''
            name = ''
            balance = 0

            try:
                bank_number = input("Please enter the bank number: ")
                name = input("Please enter the name of the bank: ")
                balance = float(input("Please enter the bank balance: "))
                if balance <= 0:
                    raise ValueError
            except ValueError:
                print("Amount would put balance below 0.")
                continue
            else:
                break

        return User.create_bank_account(bank_number, name, balance)

    @classmethod
    def generate_user(cls, **kwargs):
        """
        Create a new user by passing in all user attributes including the BankAccount attributes.
        :param kwargs:
            name: string
            age: int
            user_type: Enum category.UserType
        :return:
        """
        name = kwargs["name"]
        age = kwargs["age"]
        account_number = kwargs["account_number"]
        balance = kwargs["balance"]
        bank_name = kwargs["bank_name"]
        bank_account = BankAccount(account_number, bank_name, balance)
        bank_account.create_budgets()
        return cls(name, age, bank_account)

    @staticmethod
    def create_bank_account(bank_number, bank_name, balance):
        """
        Create a new Bank Account object with the user's bank details.
        :return: the newly created bank account object.
        """
        bank_account = BankAccount(bank_number, bank_name, balance)
        return bank_account








