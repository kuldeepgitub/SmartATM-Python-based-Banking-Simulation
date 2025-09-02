class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
                           Hello! What you want to perform?
                           Press 1 to create Pin
                           Press 2 to Deposit
                           Press 3 to Withdraw
                           Press 4 to Check Balance
                           Press 5 to Exit
                           """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Exit")
        else:
            print("Bye")

    def create_pin(self):
        self.pin = input("Enter New Pin:")
        print("Pin Created Successful!")

    def deposit(self):
        temp = input("Enter your Pin:")
        if temp == self.pin:
            amount = int(input("Enter the deposit amount:"))
            self.balance = self.balance + amount
            print("Deposit Successful!")
        else:
            print("Invalid Pin")

    def withdraw(self):
        self.withdraw = int(input("Enter the withdraw amount:"))
        temp = input("Enter your Pin:")
        if temp == self.pin:
            amount = int(input("Enter the Amount:"))
            if amount<self.balance:
                self.balance = self.balance - amount
                print("Withdraw Successful!")
            else:
                print("Insufficient Funds!")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter your Pin:")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")
sbi = Atm()
