try:
    x=int(input("enter the number:"))
    y=int(input("enter the number:"))
    print("result=",x/y)
except NameError as e:
    print("First assign/declare value ofx/y",e)
except ValueError as v:
    print("please provided specific type value",v)
except ZeroDivisionError as z:
    print("divided by zero is not posssible",z)