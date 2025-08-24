
#print a factorial number using user input.
'''n=int(input("enter the number"))
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
r=fact(n)
print(r)'''

#print a factorial number.
'''def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
r=fact(5)
print(r)'''

#sum of the number using user input.
'''def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n+fact(n-1)
n=int(input("enter the number:"))
r=fact(n)
print(r)'''

#print GCD of the two number using user input.
'''def gcd(n1,n2):
    if n2!=0:
        return (n2,n1%n2)
    else:
        return n1
m=int(input("enter the number:"))
n=int(input("enter the number:"))
gcd_result=gcd(m,n)
print("GCD=",gcd_result)'''

# print GCD number of the two numbwr without user input.
'''def gcd(n1,n2):
    if n2!=0:
        return (n2,n1%n2)
    else:
        return 1
gcd_result=gcd(10,5)
print(gcd_result)'''

#write a python programme print hello world using function.
'''def display():
    print("hello world")
display()'''

#write a python programme calculate the ncr[values of n and r taking from user]   ncr=(n!)//{r!*(n-r!)}
'''def fact(c):
    if c==0 or c==1:
        return 1
    else:
        return c*fact(c-1)
n=int(input("enter the number:"))
r=int(input("enter the number:"))
n_fact=fact(n)
r_fact=fact(r)
n_rfact=fact(n-r)
ncr=(n_fact)//(r_fact*n_rfact)
print(ncr)'''

#write a python programme calculate the npr[values of n and r taking from user]  
'''def fact(p):
    if p==0 or p==1:
        return 1
    else:
        return p*fact(p-1)
n=int(input("enter the number:"))
r=int(input("enter the number:"))
n_fact=fact(n)
r_fact=fact(r)
npr=(n_fact)//(r_fact)
print(npr)'''

 
#write a python programme fibonoci series[using recursive function]
'''def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)  #fibo(2-1)+fibo(2-2)=fibo(1)+fibo(0)=1+0=1
           # fib0(3-1)+fib0(3-2)=fibo(2)+fibo(1)=fibo(2-1)+fibo(2-2)+fibo(1)=fibo(1)+fibo(0)+fibo(1)=1+0+1=2
           # fibo(4-1)+fibo(4-2)=fibo(3)+fibo(2)=fibo(3-1)+fibo(3-2)+fibo(2-1)+fibo(2-2)=fibo(2)+fibo(1)+fibo(1)+fibo(0)
          # =fibo(2-1)+fibo(2-2)+1+1+0=fibo(1)+fibo(0)+2=3
         # fibo(5-1)+fibo(5-2)=fibo(4)+fibo(3)=fibo(4-1)+fibo(4-2)+fibo(3-1)+fibo(3-2)=fibo(3)+fibo(2)+fibo(2)+fibo(1)
         #=fibo(3-1)+fibo(3-2)+fibo(2-1)+fibo(2-2)+fibo(2-1)+fibo(2-2)+1=fibo(2)+fibo(1)+fibo(1)+fibo(0)+fibo(1)+0+1
         #=fibo(2)+1+1+0+1+0+1=fibo(2-1)+fibo(2-2)+4=1+4=5

n=int(input("enter the number:")) #n=5
if(n<0):
    print("please enter valid input")
else:
    for i in range(0,n):
        print(fibo(i),end=" ") #0,1,1,2,3,5'''



#power function using recursion:
'''def pow(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        return a*pow(a,b-1)
m=int(input("enter the base value"))
n=int(input("enter the exponetial value:"))
r=pow(m,n)
print(f"{m}^{n}=",r)'''

#frog jump:
def frog(n):
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        return frog(n-1)+frog(n-2)+frog(n-3)
h=int(input("enter height:"))
step=frog(h)
print("possible path:",step)

 
