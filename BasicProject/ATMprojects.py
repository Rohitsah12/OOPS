class Atm:
    def __init__(self):
        self.__pin=""
        self.__balance=0
        self.__menu()
    def __menu(self):
        user_input=input("""
                Welcome!! 
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit
""")
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("Thankyou!! Have a Nice Day")
    def create_pin(self):
        self.__pin=int(input("Enter your pin: "))
        print("Pin Set Sucessfully")
    
    def deposit(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            amount=int(input("Enter the amount: "))
            self.__balance=self.__balance+amount
            print("Deposit Sucessful")
        else:
            print("Invalid Pin")
    def withdraw(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            amount=int(input("Enter the amount: "))
            if amount<self.__balance:
                self.__balance=self.__balance-amount
                print("Operation Sucessful")
            else:
                print("Insufficient balance")
        else:
            print("Insufficient balance")
    
    def check_balance(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin")