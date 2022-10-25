#Atm code
class Atm:
    def __init__(self):
        pin = ""
        blance = 0

        self.menu()

    def menu(self):
        user_input = input('''
        Hello How Would You Like to Procceed?
        1. Enter 1 To Creat PIN 
        2. Enter 2 To Deposit
        3. Enter 3 To Withdraw
        4. Enter 4 To Check Blance
        5. Enter 5 To Exit
        ''')

        if user_input == "1":
            self.creat_pin()
        if user_input == "2":
            self.deposit()

        if user_input == "3":
            self.withdraw()
        if user_input == "4":
            self.blance()

    def creat_pin(self):
        self.pin = input("Input PIN")
        print("PIN creat successfully")

    def deposit(self):
        temp = int(input("Enter the PIN"))
        if temp == self.pin:
            amount = int(input("Enter The Amount"))
            self.blance = self.blance + amount
            print("deposit successfully")

        else:
            print("Incorrect Password")

    def withdraw(self):
       temp = int(input("Enter the PIN"))
       if temp == self.pin:
            amount = int(input("Enter The Amount"))
            if amount < self.blance:
                self.blance = self.blance - amount
                print("successfully withdraw")

            else:
                print("Insufficent Blance")

       else:
            print("Incorrect Password")

    def check_blance(self):
        temp = int(input("Enter the PIN"))
        if temp == self.pin:
            print(self.blance)
        else:
            print("Incorrect Password")



sajji = Atm()