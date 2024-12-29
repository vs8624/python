class Atm:
    # Special Method for declaring variables
    # Constructor - init is a Constructor
    """
    Constructor is a special method inside which the entire code gets automatically executed as soon
    as an object of this class is created
    """
    def __init__(self):
        self.pin = ""
        self.balance = 200

        print(id(self))
        self.menu()
        # print("test of object creation")

    # Navigation Menu function
    def menu(self):
        print("wow31")
        user_input = input("""
                        Hello, how would you like to proceed?
                        1. Enter 1 to create pin
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. Enter 5 to exit
        """)

        if user_input == '1':
            # print("Create Pin")
            self.create_pin()
        elif user_input == '2':
            print("deposit")
            self.deposit()
        elif user_input == '3':
            print("withdraw")
            self.withdraw()
        elif user_input == '4':
            print("Check balance")
            self.check_balance()
        else:
            print("Bye")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")
        
        self.menu()

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount you want to deposit: "))
            self.balance = self.balance + amount
            print("New balance: ")
            print(self.balance)
            print("Deposit was successful")
            self.menu()
        else:
            print("Invalid Pin")
            self.menu()

    def withdraw(self):
        temp = input("enter your pin: ")
        if temp == self.pin:
            withdraw_amount = int(input("Enter the amount you want to withdraw"))
            print(type(withdraw_amount))
            if(withdraw_amount < self.balance):
                self.balance = self.balance - withdraw_amount
                print("Withdrawal complete")
                self.menu()
            else:
                print("Not enough funds available to withdraw")
                self.menu()
        else:
            print("Invalid Pin")
            self.menu()

    def check_balance(self):
        i = 1
        while i <= 3:
            temp = input("Enter your pin: ")
            if temp == self.pin:
                print("Current Balance: ")
                print(self.balance)
                self.menu()
            else:
                print("Invalid Pin")
                i = i+1




