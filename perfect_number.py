#Check A NUMBER IS PERFECT OR NOT.
'''n=int(input("enter the number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("perfect number")
else:
    print("Not perfect number")'''

#PRINT PERFECT NUMBER BETWEEN A RANGE.
n=int(input("enter the number:"))
for i in range(1,n+1):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum=sum+j
    if(sum==i):
        print(i)