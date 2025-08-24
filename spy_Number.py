#spy number is a number sum of all digit is equal to product of all digit.

'''WAP to check a number is spy number or not.
Example:1124
sum=1+1+2+4=8,product=1*1*2*4=8'''
'''n=int(input("enter the number:"))
sum=0
product=1
while(n!=0):
    r=n%10
    sum+=r
    product*=r
    n=n//10
if(sum==product):
    print("spy number")
else:
    print("Not spy number")'''
#or
'''n=input("enter the number:")
sum=0
product=1
for  i in n:
    i=int(i)
    sum+=i
    product*=i
if(sum==product):
    print("spy number")
else:
    print("Not spy number")'''
 

#print spy number within range.
n=int(input("enter the number:"))
for i in range(1,n+1):
    sum=0
    product=1
    temp=i
    while(i!=0):
            r=i%10
            sum+=r
            product*=r
            i=i//10
    if(sum==product):
        print(temp)
     