import time
print("pleass inter your CARD")
time.sleep(5)
password=1234
pin=int(input("enter your ATM pin "))
balance=5000
if pin==password:
    while True:
        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit """
            )
        try:
            option=int(input("pleass enter your choise"))
        except:
            print("pleass enter valid option")
        if option==1:
            print(f"your updete balance is {balance}")
            print("==========================================================")
            print("==========================================================")
            print("==========================================================")
        if option==2:
            withdraw_amount=int(input("enter withdraw amount="))
            print("==========================================================")
            print("==========================================================")
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited form your account")
            print("==========================================================")
            print("==========================================================")
            print(f"your updated balance is {balance} ")
            print("==========================================================")
            print("==========================================================")
        if option==3:
            deposit_amount=int(input("enter deposit amount="))
            print("==========================================================")
            print("==========================================================")
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited form your account")
            print("==========================================================")
            print("==========================================================")
            print(f"your updated balance is {balance} ")
            print("==========================================================")
            print("==========================================================")
        if option==4:
            break
else:
    print("wrong pin pleass try again ")