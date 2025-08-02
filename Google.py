#Python program to interchange first and last elements in a list:
'''list=[12,23,34,54,45,67,76]
list.pop(0)
list.insert(0,76)
list.pop(6)
list.insert(6,12)
print(list)'''

#python program to swap two elements in a list.
'''list=[12,23,45,67,78,89,87,76,67]
print(len(list))
a=list[0]
list[0]=list[8]
list[8]=a
print(list)'''


#python i ways to find length of list.
'''list=[12,23,34,54,56,67,87]
print(len(list))'''

#maximun of two numbers in python.
'''list=[12,23,34,45,67,78,98,90]
list1=max(list)
print(list1)'''

'''list=[12,23,34,77,87,45,67,78,98,90]
list.sort(reverse=True)
print(list[0],list[1])'''

#python I ways to check if element exists in list.
'''list=[12,23,34,45,67,78,77,88]
for i in list:
    if i==23:
        print("exit") '''

#Different ways to clear a list in python.
'''list=[12,34,45,56,67,78]
list.pop(0)
list.pop(1)
list.pop(2) 
print(list)'''

#WAP to print the given number is odd or even.
'''Num=int(input("enter the number:"))
if(Num%2==0):
    print("even")
else:
    print("odd")  '''

#WAP to print the given number is positive or negative.
'''Num=int(input("enter the number:"))
if(Num>=0):
    print("positive")
else:
    print("Negative")'''

#wap to find the sum of two numbers.
'''a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print("sum=",a+b)'''

#WAP to find if the given number is prime or not.
'''Num=int(input("enter the number:"))
count=0
for i in range(1,Num):
    if(Num%i==0):
        count+=1
if(count==1):
    print("prime number")
else:
    print("Not Prime Number")'''

#WAP to find if the given number is palindrome or not.
Num=int(input("enter the number:"))
rev=0
temp=Num
while(Num!=0):
    rev=rev*10+Num%10
    Num=Num//10
if(rev==temp):
    print("palindrome")
else:
    print("Not Palindrome")


 