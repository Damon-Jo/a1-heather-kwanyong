class Bank:

    def __init__(self, user_list):
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
                self._registor_user
            elif number == 2:
                self._login_user
            elif number == 3:
                return
            else:
                print("\nError: Enter a number between 1 and 3.")

            if self._registor_user or self._login_user:
                self._main_menu()

    def registor_user(self):
        print("\n Let's register a new user!")
        print("================================")

        while True:
            try:
                name = input("What is the your child name?")
                age = int(input("How old is your child"))
                print("Select your child type between 1 and 3.")
                print("""
                1. Angel\n
                2. Troublemaker\n
                3. Rebel\n
            """)
                user_type = int(input())
                if age <= 0 or user_type <= 0 or user_type > 3:
                    raise ValueError

            except ValueError:
                print("Error: Please enter the appropriate integer number")

            if user_type == 1:
                user = Angel(name, age)
                break
            elif user_type == 2:
                user = Troublemaker(name, age)
                break
            else:
                user = Rebel(name, age)
                break

            self.current_user = user
            self._add_user_to_list(user)

            return True
