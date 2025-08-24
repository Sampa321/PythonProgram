#set is unorder and unchangeable.
'''s={1,2,4,5,8,6,7,1,2,3}
#type os s
print(type(s))
print(s)'''
#remove duplicate element from a list by using set
'''l=[1,2,3,4,5,8,6,7,1,2,4,5]
print(l)
print(set(l))'''
'''l=[]
s=set()
print(type(l))
print(type(s))'''
#how to add set element
'''s=set()
s.add(12)
s.add(13)
s.add(98)
s.add(76)
print(s)'''
#loop in set
'''name={"sampa","arpita","sandip","amit","mousumi","poulami"}
for i in name:
    print(i)'''
#update()
'''s1={1,2,4}
print(s1)
s2={"sampa","shruti","rudra","shreya"}
s1.update(s2)
print(s1)
s2.update(s1)
print(s2)'''
#how to remove set element
'''s1={1,3,4,5,7,8}
print(s1)
s1.remove(3)
print(s1)
s1.discard(100)
print(s1)'''
#wap to append a list to second list
'''list1=[]
n=int(input("enter  a list range:"))
for i in range(n):
    a=int(input(f"enter {i+1} element:"))
    list1.append(a)
list2=[]
for i in range(n):
    a=int(input(f"enter {i+1} element:"))
    list2.append(a)
for i in list1:
    list2.append(i)
print(list1)
print(list2)'''

'''import collections
l=[1,2,3,5,6,67,7,88,89,6,7,45,4,1,2,3,4,5,6]
print("my list:",l)
c=collections.Counter(l)
print(c)'''

'''#Write a python program sorting the list element with out inbuild method.
list1=[12,34,56,67,9]
length=len(list1)#5
# print(length)
for i in range(length):#0,1,2,3,4
    for j in range(length-1):#0,1,2,3
        if(list1[i]>list1[j+1]):
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
print("Sorted list:",list1)'''

'''l=set()
l.add(1)
l.add(23)
l.add(9)
l.add(5)
l.add(8)
print(l)
for i in l:
    print(i)'''

#union operation
'''s1=set()
s2=set()
n=int(input("enter your first set size:"))
for i in range(n):
    val=int(input("enter first set items:"))
    s1.add(val)
n1=int(input("enter your second set size:"))
for i in range(n1):
    val=int(input("enter second set items:"))
    s2.add(val)
print("set1=",s1)
print("set2=",s2)
s3=s1.union(s2)
print(s3)'''

'''s1=set()
s2=set()
n=int(input("enter your first set size:"))
for i in range(n):
    val=int(input("enter first set items:"))
    s1.add(val)
n1=int(input("enter your second set size:"))
for i in range(n1):
    val=int(input("enter second set items:"))
    s2.add(val)
print("set1=",s1)
print("set2=",s2)
s1.update(s2)
print(s1)'''

'''s1=set()
s2=set()
n=int(input("enter your first set size:"))
for i in range(n):
    val=int(input("enter first set items:"))
    s1.add(val)
n1=int(input("enter your second set size:"))
for i in range(n1):
    val=int(input("enter second set items:"))
    s2.add(val)
print("set1=",s1)
print("set2=",s2)
s3=s1.difference(s2)
s4=s1-s2
print(s3)
print(s4)'''

#intersection
'''s1=set()
s2=set()
n=int(input("enter your first set size:"))
for i in range(n):
    val=int(input("enter first set items:"))
    s1.add(val)
n1=int(input("enter your second set size:"))
for i in range(n1):
    val=int(input("enter second set items:"))
    s2.add(val)
print("set1=",s1)
print("set2=",s2)
s3=s1.intersection(s2)
s4=s1&s2
print(s3)
print(s4)'''

#convert list to set and print intersection
'''l=[1,8,9,3,5,7]
l1=[9,5,12,35,7,11]
s=set(l)
s1=set(l1)
s2=s.intersection(s1)
print(s2)'''

 