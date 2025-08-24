#print a number prime or not.
'''n=int(input("enter the number:"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==2):
    print("prime number")
else:
    print("not prime number")'''

#print prime number of 100 to 200.
a=int(input("enter the number:"))
b=int(input("enter the number:"))
for i in range(a,b+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if(count==2):
        print(i)

