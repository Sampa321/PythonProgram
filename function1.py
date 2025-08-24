#function:
'''print("bhaskar")
print("bhaskar")
print("bhaskar")
print("bhaskar")
#declaration python function:-
def  myname(a,b):
    if a>b:
        print(a)
    else:
        print(b)
myname(12,34)'''

'''def myname(a,b):
    if a>b:
        print(a)
    else:
        print(b)
p=int(input("enter your 1st item:"))
q=int(input("enter your 2nd item:"))
myname(p,q)'''

#print sum of two number using function:
'''def sum(a1,b1):
    return a1+b1
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
sum(a,b)
print("sum =",sum(a,b))'''

#calculate the area and perimeter of a circle:
'''r=int(input("enter the circle radius="))
pi=3.14
def area(r1,p):
    return p*r1*r1
def perimeter(r2,p):
    return 2*p*r2
print("area=",area(r,pi))
print("perimeter=",perimeter(r,pi))'''

#sum of all list item using function.
'''l=[12,3,5,6,7]
sum=0
for i in l:
    sum+=i
print(sum)'''

'''def listsum(l):
    sum=0
    for i in l:
        sum+=i
    return sum
l1=[]
r=int(input("enter the list range:"))
for i in range(r):
    val=int(input("enter the list element:"))
    l1.append(val)
print(l1)
sum1=listsum(l1)
print(sum1)'''

#mulplication of all list item using function.
'''l=[1,2,3,5]
mul=1
for i in l:
    mul*=i
print(mul)''' 

'''def listmul(l):
    mul=1
    for i in l:
        mul*=i
    return mul
l1=[]
r=int(input("enter the list range:"))
for i in range(r):
    val=int(input("enter the list element:"))
    l1.append(val)
print(l1)
mul1=listmul(l1)
print("mul=",mul1)'''

#maximum and minimum list item using function.
'''def max_item(l):
    return max(l)
def min_item(l):
    return min(l)
l1=[]
r=int(input("enter the list range:"))
for i in range(r):
    val=int(input("enter the list element:"))
    l1.append(val)
max=max_item(l1)
min=min_item(l1)
print("max value=",max)
print("min value=",min)'''

#no of uppercase and lowercase in string.
'''str=input("enter the string:")
lower=0
upper=0
for i in str:
    if(i>='a' and i<='z'):
        lower+=1
    elif(i>='A' and i<='Z'):
        upper+=1
    else:
        pass
print(f"upper={upper} and lower={lower}")'''

'''def upper_lower(str):
    upper=0
    lower=0
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        else:
            pass
    print(f"original str={str} upper_case={upper} and lower_case={lower}")
upper_lower("sampa NAYAK")'''

#print ncr value.
'''def fact(n1):
    fact=1
    for i in range(1,n1+1):
        fact*=i
    return fact
n=int(input("enter the value of n:"))
r=int(input("enter the value of r:"))
nfact=fact(n)
rfact=fact(r)
n_rfact=fact(n-r)
ncr=(nfact)//(rfact*n_rfact)
print("ncr=",ncr)'''

#print npr value.
def fact(n1):
    fact=1
    for i in range(1,n1+1):
        fact*=i
    return fact
n=int(input("enter the value of n:"))
r=int(input("enter the value of r:"))
nfact=fact(n)
n_rfact=fact(n-r)
npr=(nfact)//(n_rfact)
print("npr=",npr)


