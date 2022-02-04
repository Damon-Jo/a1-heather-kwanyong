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

    # Properties
    remaining_balance = property(get_remaining_balance)
    expenses = property(get_expenses)

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

    def get_budgets(self):
        """
        Return the current status of user's budgets from all categories.
        :return:
        """
        # TODO: More logic required on determining locked account.
        if self._is_locked:
            return True
        # TODO: math needed to added for each category
        print("--- Current account status --- "
              "Amount spent: ", self.remaining_balance,
              "Remaining amount: \n"
              "1. Games and Entertainment: ",
              "2. Clothing and Accessories: ",
              "3. Eating out: " ,
              "4. Miscellaneous: ",)



    def prompt_record_transaction(self) -> None:
        """
        Prompt inputs to user asking for details of a new transaction.
        """
        string_input = input("Please enter the following details to create a transaction.")
        user_input = int(string_input)
        try:
            if user_input == '':
                print("Please enter valid number between 1 - 4.")
                pass
        except ValueError:
            print("Invalid input. Please enter valid number between 1 -4.")
        else:
            # TODO: Is the timestamp going to be current time?
            input_timestamp = datetime.now()
            input_budget_category = int(input("Please enter the category: \n"
                                              "1. Games and Entertainment\n"
                                              "2. Clothing and Accessories\n"
                                              "3. Eating out\n"
                                              "4. Miscellaneous\n"))
            input_dollar_amount = int(input("Please enter the amount: "))

            input_expense_location = input("Please enter the name of "
                                           "the shop/website where the purchase took place: ")

            new_transaction = Transaction(input_timestamp, input_budget_category,
                                          input_dollar_amount, input_expense_location)


    def transactions_by_budget(self) -> list:
        """
        Return a list of transactions by budget category selected by an user.
        :return: a list of transactions
        """
        string_input = input("Please enter one budget category you would like to see: \n"
                             "1. Games and Entertainment\n"
                             "2. Clothing and Accessories\n"
                             "3. Eating out\n"
                             "4. Miscellaneous\n")
        user_input = int(string_input)
        try:
            # TODO: add logics to retrieve transactions.
            if user_input == 1:
                print("*** The list of transaction in Games and Entertainment ***\n"
                      "")

            elif user_input == 2:
                print("*** The list of transaction in Clothing and Accessories ***\n"
                      "")

            elif user_input == 3:
                print("*** The list of transaction in Eating out ***\n"
                      "")

            elif user_input == 4:
                print("*** The list of transaction in Miscellaneous ***\n"
                      "")

        except ValueError:
            print("Invalid input. Please enter valid number between 1 -4.")

        else:
            print("Please enter valid number between 1 - 4.")
            pass



