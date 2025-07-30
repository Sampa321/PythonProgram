#PRINT A NUMBER IS ARMSTRONG OR NOT.
n=int(input("enter the number:"))
rem=0
sum=0
temp=n
while(n!=0):
    rem=n%10
    sum=sum+pow(rem,3)
    n=n//10
if(sum==temp):
    print("Armstrong number")
else:
    print("Not Armstrong number")

#print armstrong numbers within a range.
# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     rem=0
#     sum=0
#     temp=i
#     while(i!=0):
#         rem=i%10
#         sum=sum+pow(rem,3)
#         i=i//10
#     if(sum==temp):
#         print(temp)