#list: list is a data structure where we can store mutiple data.
'''list=[12,13,14,15,56,78,87]
print(list[2])
print(list)
print(len(list))
print(type(list)) '''

#index
'''for i in range(0,len(list)):
    print(list[i])'''
#or,
'''for i in list:
    print(i)'''

#add element in a list.
'''list.append(89)
print(list)'''

#add element in a list of a position.
'''list.insert(2,98)
print(list)'''

#print ascending order.
'''list.sort()
print(list)'''

#print discending order.
'''list.sort(reverse=True)
print(list)'''

#remove duplicate element in a list.
'''l1=[12,98,87,76,65,54,43,32,12,98]
print(l1)
print(set(l1))'''

#remove duplicate element using set.
'''s={12,98,87,76,65,54,43,32,12,98}
print(s)'''
 
#print max element in a list.
'''l1=max([12,14,35,76,86,98,78,56])
print(f"max=",l1)'''
#print min element in a list.
'''l2=min([12,14,35,76,86,98,78,56])
print(f"min=",l2)'''

#add element in a list of a position and remove element this position.
'''l[2]=89
print(l)'''