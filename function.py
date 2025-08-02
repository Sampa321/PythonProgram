'''A FUNCTION IS  A BLOCK OF CODE WHICH ONLY RUNS WHEN IT IS CALLED.YOU CAN PASS DATA,KNOWN AS PARAMETERS,INTO A 
FUNCTION.A FUNCTION CAN RETURN DATA AS A RESULT.SMALLEST SAGMENT OF ALARGE PROGRAMME IS CALLED FUNCTION.'''

#use for function call many times.
'''def display():
    print("I am sampa Nayak")
display()
display()
display()'''

#print for 100 times:
'''def display():
    print("sampa nayak")
for i in range(100):
    display()'''

#write a programme addition,substruction,multiplication,division,module using function:
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
def add():
    print("add=",a+b)
def sub():
    print("sub=",a-b)
def mul():
    print("mul=",a*b)
def div():
    print("div=",a/b)
def mod():
    print("mod=",a%b)
add()
sub()
mul()
mod()
div()