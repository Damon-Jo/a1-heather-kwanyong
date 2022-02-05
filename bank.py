from pandocfilters import Null

from user import User

from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel


class Bank:
    """
    Class representing a Family Appointed Moderator (F.A.M.)
    """

    def __init__(self, user_list: list):
        self._user_list = user_list
        self._current_user = None

    def get_current_user(self):
        """
        Get the user that is currently logged in.
        :return: a User
        """
        return self._current_user

    def set_current_user(self, user):
        """
        Set the user that is currently logged in.
        :param user: a User
        """
        self._current_user = user

    def get_user_list(self):
        """
        Retrieve the FAM user list.
        :return: the user list as a list
        """
        return self._user_list

    def set_user_list(self, user_list):
        """
        Set the user list to the value passed in.
        :param user_list: a list of Users
        """
        self._user_list = user_list


    def _add_user_to_list(self, user):
        """
        Add a user to the list.
        :param user: the User object to be added to the list of users
        """
        self._user_list.append(user)

    def _show_registration_menu(self):
        """
        Show the menu for registering a new user to the system.
        """

        # register the user
        self._register_user()

    def _register_user(self):
        """
        Prompt user to enter their details and add them to the user list.
        :return: True always
        """
        print("\n Let's register a new user!")
        print("================================")

        while True:
            try:
                name = input("What is the your child name?")
                age = int(input("How old is your child?"))
                print("---------------------------------------")
                print("Select your child type between 1 and 3.")
                print("1. Angel")
                print("2. Troublemaker")
                print("3. Rebel")
                print(">>", end="")
                user_type = int(input())
                if age <= 0 or user_type <= 0 or user_type > 3:
                    raise ValueError
            except ValueError:
                print("Error: Please enter the appropriate integer number")
                continue

            if user_type == 1:
                user = Angel(name, age)
                break
            elif user_type == 2:
                user = Troublemaker(name, age)
                break
            elif user_type == 3:
                user = Rebel(name, age)
                break
            else:
                print("\nError: Please enter a valid number. Please try again.")

        self.current_user = user
        self._add_user_to_list(user)

        return True

    def _main_menu(self):
        """
        Show the actions menu and takes input from the user.
        """
        while True:
            # Check if a user is locked, if so exit out of the actions menu
            if self.current_user.can_lock_account():
                raise UserIsLockedError("Your account is locked. We have logged you out")

            print(f"\nLogged in as {self.current_user.name}\n")

            # options:

            print("---------------------------")
            print("1. View Budgets")
            print("2. Record Transaction")
            print("3. View Transaction by Budget")
            print("4. View Bank Account Details")
            print("5. Quit")
            print("---------------------------")



            try:
                number = int(input("Select a number!"))
            except ValueError:
                print("Error: Please enter the number! Please try again.")
                continue
            # choose 5 : LOGOUT, back to main menu
            if number == 5:
                return
            else:
                # performs the action selected by the user.
                self._perform_action(number)

    def _perform_action(self, option):
        """
        Perform an action based on the option selected by a user.
        :param option: an int
        """
        if option == 1:
            self.current_user.view_budgets()
        elif option == 2:
            self.current_user.record_transaction()
        elif option == 3:
            self.current_user.view_transactions()
        elif option == 4:
            self.current_user.view_bank_details()
        else:
            print("Please enter a valid option.")

    def _login_user(self):
        """
        Display the user list to log in.
        :return: True whether login succeeds or False login fails
        """
        # Display list of users and prompt an input

        print("\n---- User List ----")

        for index, user in enumerate(self.user_list):
            print(f"{index+1} - {user}")

        # Exit if the last option is chosen
        exit_option = len(self.user_list) + 1
        print(f"{exit_option} - Back to main menu")

        valid_users = range(1, len(self.user_list) + 1)
        choice = 0
        while True:
            try:
                choice = int(input("Please choose the user : "))
            except ValueError:
                print("\nError: Please enter a valid number. Please try again.")
                continue

            # Loop until a valid user is selected
            if choice in valid_users:
                break
            elif choice == exit_option:
                return False
            else:
                print("\nError: Please enter a valid number. Please try again.")

        # Set current user to selected user
        self.current_user = self.user_list[choice - 1]
        return True

    def start_menu(self):
        while True:
            print("\nWelcome to the Family Appointed Moderator!")
            print("---------------------------")
            print("1. Resister new user\n")
            print("2. Login\n")
            print("3. Exit\n")

            try:
                number = int(input("Select a number>>"))
            except ValueError:
                print("Error: Please enter the number>>")
                continue

            number
            {
                1: self._register_user,
                2: self._login_user,
                3: self._quit
            }.get(number)()

            if self._register_user or self._login_user:
                self._main_menu()

    def _quit(self):
        """ Quit the FAM Program. """
        print("The program exited!")
        exit()

    @staticmethod
    def load_test_user():
        """
        Return a test user for developing purposes.
        return: a test user as a User object
        """
        return Angel("Bob", 25)
