#delete element in a list of a position.
list=[12,14,45,67,87,78,98]
list.pop(0)
print(list)   #delete first element

#create a user input list and ascending and descending order list.
'''list=[]
for i in range(9):
    a=int(input("enter the element:"))
    list.append(a)
print(list)
# list=[12,14,45,67,87,78,98]
list.sort()
print(f"ascending=",list)
list.sort(reverse=True)
print(f"descending=",list)'''


#remove duplicate element in a list.
'''list=[34,45,67,87,98,34,45]
print(list)      #original list
s={34,45,67,87,98,34,45}
print(s)
print(set(list))'''       #remove duplicate element


#question-5:( print Even or odd in a list))
'''l=[]
l1=[]
l2=[]
for i in range(9):
    a=int(input("enter list element:"))
    l.append(a)
for i in l:
    if(i%2==0):
        l1.append(i)
    else:
         l2.append(i)
print(f"EVEN_numbers={l1} ODD_numbers={l2}")'''

#create a user input list and store element in a list which is divided M and N(M and N is a number).
'''l1=[]
l2=[]
M=int(input("enter the value of M:"))
N=int(input("enter the value of N:"))
for i in range(10):
    a=int(input("enter list element:"))
    l1.append(a) 
print(f"l1={l1}")
for i in l1:
    if(i%M==0 and i%N==0):
        l2.append(i)
print(f"divisible_by M and N={l2}")'''

# QUESTION-7;(USER INPUT A LIST THEN OTHER LIST ADD PRIME NUMBER)
'''list=[]
prime_list=[]
for i in range(10):
    a=int(input("enter the number:"))
    list.append(a)
print(list)
for i in list:
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=count+1
    if(count==0):
        prime_list.append(i)
print(prime_list)'''



#MULTIPLE NUMBERS CHECK IN A LIST:
'''my_array = [1, 2, 3, 4, 5]
numbers_to_check = [2, 5, 7]

if all(num in my_array for num in numbers_to_check):
    print("All numbers exist in the array.")
else:
    print("Not all numbers exist in the array.")'''


#Question-8(Take a user input list, and separate all the palindrome numbers present in the list)
'''list=[]
l1=[]
for i in range(5):
    a=int(input("enter the list element:"))
    list.append(a)
for i in list:
    rem=0
    rev=0
    temp=i
    while i!=0:
        rem=i%10
        rev=rev*10+rem
        i=i//10
    if(rev==temp):
        l1.append(temp)
print(l1)'''

 #other process:
 
'''def  checkpalindrome(num):
    s=str(num)
    p=s[::-1]
    if s==p:
        return 1
    else:
        return 0

limit2=int(input("enter the limit:"))
l=[]
cl=[]
for i in range(0,limit2):
    b=int(input("enter the number:"))
    l.append(b)
    if checkpalindrome(b)==1:
        cl.append(b)
print("actual list:",l)
print("list with palindrome elements",cl)'''

#store palindrome number in a list.
'''l=[]
for i in range(1,100):
    rev=0
    temp=i
    while i!=0:
        rev=rev*10+i%10
        i=i//10
    if(rev==temp):
        l.append(temp)
print(l)'''
 