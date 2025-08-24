'''l=[]  #empty list
print(type(l))
print(l)
l1=[1,2,3,45,545,"sampa","arpita","sandip"]
print(type(l1))
#append()....to add element in list
l.append(12)
l.append("amit")
l.append(90.12)
print(l)
for i in l:
    print(i)'''

#print first 30 number.
'''num=[]
for i in range(31):
    num.append(i)
print(num)'''

#print all odd number within 50.
'''odd_Num=[]
for i in range(51):
    if(i%2==1):
        odd_Num.append(i)
print(odd_Num)'''

'''odd_Num=[]
for i in range(1,51,2):
    odd_Num.append(i)
print(odd_Num)'''

#print all even number within 50.
'''even_Num=[]
for i in range(1,51):
    if(i%2==0):
        even_Num.append(i)
print(even_Num)'''

'''even_Num=[]
for i in range(2,51,2):
    even_Num.append(i)
print(even_Num)'''

#sum of firat 50 numbers.
'''sumNum=[]
sum=0
for i in range(1,51):
    sumNum.append(i)
print(sumNum)
for i in sumNum:
    sum+=i
print(sum)'''

'''sum=0
for i in range(51):
    sum+=i
print(sum)'''

#sum of even and odd
''''even_sum=0
odd_sum=0
n=int(input("enter the range:"))
for i in range(n):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print(f"sum of even number={even_sum} sum of odd number={odd_sum}")'''


'''l=[]
rang=int(input("enter the range:"))
for i in range(rang):
    val=int(input("enter the value:"))
    l.append(val)
print(l)

#list element access using loop.
for i in l:
    print(i)
#list element access using index.
print(l[2])
for i in range(rang):
    print(i)'''

#create a empty list and take 6 input from user and print odd position element.
'''list=[]
r=int(input("enter the range:"))
for i in range(r):
    value=int(input("enter the list element:"))
    list.append(value)
print(list)
for i in range(r):
    if i%2!=0:
        print(list[i])'''

#create a empty list and take 6 input from user and print even position element.
'''list=[]
r=int(input("enter the range:"))
for i in range(r):
    value=int(input("enter the list element:"))
    list.append(value)
print(list)
for i in range(r):
    if i%2==0:
        print(list[i])'''

#sum of all list element. 
'''l=[]
sum=0
r=int(input("enter the range:"))
for i in range(r):
    val=int(input("enter the list element:"))
    l.append(val)
print(l)
#process1
for i in l:
    sum+=i
print(sum)
#process 2
for i in range(r):
    sum+=l[i]
print(sum)'''

#sum of all odd element in list.
'''list=[]
sum=0
r=int(input("enter the range:"))
for i in range(r):
    val=int(input("enter the list element:"))
    list.append(val)
#process 1
for i in list:
    if i%2!=0:
        sum+=i
print(sum)
#process 2
for i in range(r):
    sum+=list[i]
print("sum=",sum)'''

#l=[10,11,45,22,9,55,21,42,63]print those element which are divisible by 3 and 7.
'''l=[10,11,45,22,9,55,21,42,63]
print("divisible by 4 and 7:")
for i in l:
    if(i%3==0 and i%7==0):
        print(i)'''

#l=[1,3,4,2,6,8,9] print even or odd element in different list.
'''l=[1,3,4,2,6,8,9]
even_list=[]
odd_list=[]
for i in l:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print(f"even list={even_list} odd list={odd_list}")'''

#list inbuild method.
'''l=[1,2,3]
print(l)
l1=[12,23]
l.append(l1)
print(l)
#insert(position,item)
l.insert(1,9)
print(l)'''

#check a element is present how many times.
'''l=[1,2,3,1,1,23]
print("how many times present 1 in l:",l.count(1))'''

'''list=[]
r=int(input("enter the range:"))
for i in range(r):
    num=int(input("enter the list element:"))
    list.append(num)
print(list.count(1))'''

#delete element in a list.
'''list=[12,34,55,67,75,77]
list.pop(3)
print(list)
list.pop()
print(list)'''

'''l=[11,1,8,9,8,77,55,66]
#del l[1:5]
l.remove(8)
print(l)'''

#print maximum and minimum element in a list.
'''list=[12,23,45,22,90,4,45]
l1=max(list)
l2=min(list)
print(f"maximum element={l1} minimum element={l2}")'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

#reverse a list.
'''list=["sampa","arpita","shreya","shruti","sangita"]
list.reverse()                                
print(list)'''

#sorting accending and decending .
'''l=[12,233,45,2,34,67,90,9,89]
#accending
l.sort()
print("accending=",l)
#decending
l.sort(reverse=True)
print("decending=",l)'''

#sum of second maximum number and second minimum number of a list.
'''l=[12,3,4,32,90,99,89,34,67]
l.sort()
l1=l
print(l1)
M=l1[1]
l.sort(reverse=True)
l2=l
print(l2)
m=l2[1]
print(M+m)'''

'''l=[12,3,4,32,90,99,89,34,67]
length=len(l)
print(length)
l.sort()
sec_min=l[1]
sec_max=l[length-2]
print(sec_min+sec_max)'''

#create a list and take 8 input from user l=[21,45,42,78,77,44,88,99] print those item which are divisivle by 3 and 2.
'''list=[]
r=int(input("enter the range:"))
for i in range(r):
    n=int(input("enter the list element:"))
    list.append(n)
for i in list:
    if(i%3==0 and i%2==0):
        print(i)'''

#Remove duplicate element from a list.
'''list=[12,23,34,12,23,34,45,56,67,8,99]
list1=set(list)
print(list1)'''

'''l=[1,8,9,3,5,7]
l1=[9,5,12,35,7,11]
s=set(l)
s1=set(l1)
s2=s.intersection(s1)
print(s2)'''

#WAP print that all posible pair of a list:
'''l=[]
n=int(input("enter the list range:"))
for i in range(n):
    val=int(input("enter the list element:"))
    l.append(val)
for i in range(n):
    for j in range(i+1,n):
        print((l[i],l[j]))'''


#WAP print that sum of product all posible pair of a list:
'''l=[]
sum=0
n=int(input("enter the list range:"))
for i in range(n):
    val=int(input("enter the list element:"))
    l.append(val)
for i in range(len(0,l)):
    for j in range(i+1,len(l)):
        sum=sum+l[i]*l[j]
print(sum)'''

#WAP print search element that all posible pair sum of a list:
'''l=[]
n=int(input("enter the list range:"))
for i in range(n):
    val=int(input("enter the list element:"))
    l.append(val)
search=int(input("enter the search element:"))
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
         for k in range(j+1,len(l)):
            if l[i]+l[j]+l[k]==search:
                print((l[i],l[j],l[k]))'''
             

 