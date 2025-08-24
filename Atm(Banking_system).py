class Atm:
    #constractor
    def __init__(self):
        self.pin='' #5566
        self.amount=0
        self.menu()
    def menu(self):
        user_input=input("How can i help you 1.Press 1 for create pin 2.Press 2 to change pin 3.press 3 to check balance")
        if(user_input=='1'):
            self.create_pin()
        elif(user_input=='2'):
            self.change_pin()
        elif(user_input=='3'):
            self.check_balance()
        elif(user_input=='4'):
            self.balance_withdraw()
        else:
            exit()
    def create_pin(self):
        user_pin=input("Enter your pin:")
        self.pin=user_pin
        user_balance=int(input("Enter your amount:"))
        self.amount=user_balance
        print("Balance Deposit successful")
        self.menu()
    def change_pin(self):
        old_pin=input("Enter your old pin:")
        if(old_pin==self.pin):
            new_pin=input("enter your new pin:")
            self.pin=new_pin
            print("pin change successfully")
        else:
            print("Please enter your correct pin")
            self.menu()
    def check_balance(self):
        user_pin=input("Enter your pin")
        if(self.pin==user_pin):
            print("Your current balance=",self.amount)
        else:
            print("Please enter your correct pin try again")
            self.menu()
    def balance_withdraw(self):
        user_pin=input("Enter your pin:")
        if(user_pin==self.pin):
            amount=int(input("enter withdraw amount:"))
            if(amount<=self.amount):
                self.amount=self.amount-amount
                print("Withdraw successfuly and your current balance",self.amount)
            else:
                print("insufficient balance")
        else:
            print("please enter your correct pin")
        self.menu()
obj=Atm()