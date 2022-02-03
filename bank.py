from user import User

from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel


class Bank:

    def __init__(self, user_list: list):
        self._user_list = user_list

    def start_menu(self):
        while True:
            print("""
                1. Resister new user\n
                2. Login\n
                3. Exit\n
            """)

            try:
                number = int(input("Select a number!"))
            except ValueError:
                print("Error: Please enter the number!")
                continue

            if number == 1:
                self._register_user
            elif number == 2:
                self._login_user
            elif number == 3:
                return
            else:
                print("\nError: Enter a number between 1 and 3.")

            if self._registor_user or self._login_user:
                self._main_menu()



    @staticmethod
    def register_user():
        print("\n Let's register a new user!")
        print("================================")

        while True:
            try:
                name = input("What is the your child name?")
                age = int(input("How old is your child"))
                print("Select your child type between 1 and 3.")
                print("1. Angel\n")
                print("2. Troublemaker\n")
                print("3. Rebel\n")

                user_type = int(input())
                if age <= 0 or user_type <= 0 or user_type > 3:
                    raise ValueError

            except ValueError:
                print("Error: Please enter the appropriate integer number")

            account_number = input("Enter your account number>>")

            while True:
                try:
                    balance = float(input("Current balance: "))
                except ValueError:
                    print("\nError : Please enter a valid amount")
                else:
                    if balance <= 0:
                        print("\nError : Please enter a positive amount")
                    else:
                        break

            bank_name = input("Please enter your child's bank: ")
            budgets = None
            bank_info = {
                "name": name,
                "age": age,
                "user_type": user_type,
                "account_number": account_number,
                "balance": balance,
                "bank_name": bank_name,
                "budgets": budgets
            }
           # return bank_info

            if user_type == 1:
                user = Angel.generate_user(**bank_info)
                break
            elif user_type == 2:
                user = Troublemaker.generate_user(**bank_info)
                break
            else:
                user = Rebel.generate_user(**bank_info)
                break

            # self.current_user = user
            # self._add_user_to_list(user)
            self._user_list.append(user)
            return True
