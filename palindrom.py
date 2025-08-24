#print a string is palindrome or not.
'''name=input("enter the string")
rev_str=''
for i in range(1,len(name)+1):
    rev_str=rev_str+name[-i]
if name==rev_str:
    print("palindrome")
else:
    print("not palindrome")'''

#print a integer is palindrome or not.
'''n=int(input("enter the number:"))
rev=0
temp=n
while(n!=0):
    rev=rev*10+n%10
    n=n//10
if(rev==temp):
    print("Palindrom")
else:
   print("not palindrom")'''

#PRINT PALINDROME NUMBER BETWEEN A RANGE.
n=int(input("enter the number:"))
a=int(input("enter the number:"))
for i in range(n,a+1):
    rem=0
    sum=0
    temp=i
    while i!=0:
        rem=i%10
        sum=sum*10+rem
        i=i//10
    if(sum==temp):
        print(temp)
