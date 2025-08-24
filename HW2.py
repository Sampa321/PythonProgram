#BITWISE OPERATOR
   #XOR(Exclusive-OR)
'''X=int(input("enter the value of X:"))
Y=int(input("enter the value of Y:"))
Z=X^Y
print("XOR of X and Y:",Z)'''


    #left shift
'''x=int(input("enter the value:"))
leftShift =int(input("enter the left shift:"))
z=x<<leftShift 
print(" The value of x:",z)'''


    #Right shift
'''x=int(input("enter the value:"))
rightShift =int(input("enter the shift shift:"))
z=x>>rightShift 
print(" The value of x:",z)'''


#wap swap two no using 3rd variables.
'''a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print("Before swaping,""a=",a,"b=",b)
c=a
a=b
b=c
print("After swaping,""a=",a,"b=",b)'''


#wap swap two no without using 3rd variable.
'''a=int(input("enter the value of a:"))    #10
b=int(input("enter the value of b:"))     #5
print("Before swaping,""a=",a,"b=",b)
a=a+b   #15
b=a-b   #10
a=a-b   #5
print("After swaping,""a=",a,"b=",b)'''


#wap swap two no without using 3rd variable.(ExcLusive-OR)
a=int(input("enter the value of a:"))    #10
b=int(input("enter the value of b:"))     #5
print("Before swaping,""a=",a,"b=",b)
a=a^b   #15
b=a^b   #10
a=a^b   #5
print("After swaping,""a=",a,"b=",b)