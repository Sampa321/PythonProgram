'''ARRAY IS A CONTAINER/VARIABLE WHERE WE CAN STORE MULTIPLE DATA BUT WHICH ARE SIMILAR TYPES.'''

'''import array as arr
ar1=arr.array('i',[1,2,3,4,5,6,7]) #index:0-value:1
ar1[0]=56
print(ar1) #output:56,2,3,4,5,6,7
print(ar1[1:4]) #element:2,3,4
ar1.append(58) 
print(ar1) #56,2,3,4,5,6,7,58
print(ar1.count(2)) #output:1
ar1.reverse()
print(ar1) #output:58,7,6,5,4,3,2,56'''

#knowledge for unorder:
'''dic={"carpa",12,"false",3.4}
for item in dic:
    print(item)'''

#knowledge for unorder:
'''info={11,12,13,34,48,78,98,99}
for item in info:
    print(item)'''

#user input of array element:
'''import array as arr
r=arr.array('i',[])
n=int(input("enter the size of an array element:"))
for i in range(n):
    a=int(input("enter the array element:"))
    r.append(a)
print(r)'''

#convert array to list:
'''import array as arr
r=arr.array('i',[])
list=[]
n=int(input("enter the range og array element:"))
for i in range(n):
    a=int(input("enter the array element:"))
    list.append(a)
print(list)'''

#convert array to list and remove duplicate element:
'''import array as arr
r=arr.array('i',[])
list=[]
n=int(input("enter the range of an array element:"))
for i in range(n):
    a=int(input("enter the array element:"))
    r.append(a)
for i in r:
    list.append(i)
print("original array:",r)
print("your list:",list)
print("after remove duplicate element:",set(list))'''
#other process:(remove duplicate element from array)
'''import array as arr
r=arr.array('i',[])
r1=arr.array('i',[])
n=int(input("enter the range of an array element:"))
for i in range(n):
    a=int(input("enter the array element:"))
    r.append(a)
for i in r:
    if i not in r1:
        r1.append(i)
print("remove dubplicate array element:",r1)'''
#other process(remove duplicate element from array):
'''import array as arr
r=arr.array('i',[])
n=int(input("enter the range of an array element:"))
for i in range(n):
    a=int(input("enter the array element:"))
    r.append(a)
print("original element:",r)
print("after remove duplicate element:",set(r))'''

#convert set to list:
'''set={12,23,45,44,67,78}
a=list(set)
print("list:",a)'''

#question-1(WAP to remove a specified item using the index of an array taking from user input):
'''import array as arr
r=arr.array('i',[])
n=int(input("enter the range of an array element:"))
for i in range(n):
    a=int(input("enter the array element:"))
    r.append(a)
print("original array:",r)
r.pop(3)
print("after remove of array element:",r)'''

#question-2(WAP to convert an array to an array of machine values and return the bytes representation)
'''import array as arr
r=arr.array('b',[])
n=int(input("enter the range of an element:"))
for i in range(n):
    a=int(input("enter the array element:"))
    r.append(a)
print("original array:",r)
c=r.tobytes()
print(c)'''

#question-3(WAP to append items to a specified list[list input taking from user])
'''import array as arr
r=arr.array('i',[])
list=[]
n=int(input("enter the range pf an array element:"))
for i in range(n):
    a=int(input("enter the array element:"))
    list.append(a)
print(list)
for i in list:
    r.append(i)
print(r)'''

#count number which divided a number within a range:
'''import array as arr
r=arr.array('i',[])
count=0
a=int(input("enter the number:"))
n=int(input("enter the range of an array element:"))
for i in range(n):
    b=int(input("enter the array element:"))
    r.append(b)
for i in r:
    if(i%a==0):
        count=count+1
print(count)'''

#MULTIPLE NUMBER PRINT IN A ARRAY:
'''list=[12,23,34,34,23,12,56,78,77]
uniquelist=[]
duplicatelist=[]
for i in list:
    if i not in uniquelist:
        uniquelist.append(i)
    else:
        if i not in duplicatelist:
            duplicatelist.append(i)
print(duplicatelist)
import array as arr
r=arr.array('i',duplicatelist)
print("multiple number=",r)'''


#MULTIPLE NUMBERS CHECK IN A ARRAY.
import array as arr

my_array = arr.array('i', [1, 2, 3, 4, 5])
numbers_to_check = [2, 5, 1]

if all(num in my_array for num in numbers_to_check):
    print("All numbers exist in the array.")
else:
    print("Not all numbers exist in the array.")