'''PYTHON LAMBDA FUNCTIONS ARE ANONYMOUS FUNCTIONS MEANS THAT THE FUNCTION IS WITHOUT A NAME.AS WE ALREADY KNOW THE DEF
KEYWORD IS USED TO DEFINE A NORMAL FUNCTION IN PYTHON.SIMILARLY,THR LAMBDA KEYWORD IS USED TO DEFINE ANANONYMOUS FUNCTION
IN PYTHON.'''

# ADD AND MULTIPLE TWO NUMBERS USING LAMBDA FUNCTION.
'''a=int(input("enter the number:"))
b=int(input("enter the number:"))
f=lambda a,b:a+b
result=f(a,b)  
print("add=",result)
f1=lambda a,b:a*b
result1=f1(a,b)
print("mul=",result1)'''

#PRINT EVEN NUMBER LIST USING LAMBDA FUNCTION.                                                                                                                                                                                                                                                                     
'''num=[12,34,54,55,66,78,67,97]                                                                                                                                                                                                                                                                                                                                                                            
even_number=list(filter(lambda n:n%2==0,num))
print("even_number=",even_number)'''

#Create a list take user input and it's divided another two list(even number list,odd number list) using lambda 
'''list1=[]
even=[]
odd=[]
for i in range(5):
    a=int(input("enter the list element:"))
    list1.append(a)
even_list=lambda x: x%2==0
for i in range(0,len(list1)):
    if even_list(list1[i]):
        even.append(list1[i])
    else:
        odd.append(list1[i])
print("even_list:",even)
print("odd_list:",odd)'''


# create a list insite the list create atleast 5 dictenary store state with respect to capital finally sortedlist based on their capital name.
'''state_capi=[{'state':'West bengal','capital':'Kolkata'},{'state':'Bihar','capital':'Patna'},
            {'state':'Asam','capital':'Dispur'},{'state':'Goa','capital':'Panaji'},
            {'state':'Gujrat','capital':'Gandhinagar'}]
print(state_capi)
sorted_capi=sorted(state_capi,key=lambda x:x ['capital'])
print(sorted_capi)          
'''
'''num=[12,34,4,56,78,3,15]
even_number=list(filter(lambda n:n%2==0 and n>50,num))
print(even_number)'''

'''city=['asam','jaipur','kota','west bengal']
length_city=sorted(city,key=lambda x: len(x),reverse=True)
print(length_city)'''

'''f=lambda:print("Hello world")
f()'''

#create a dictionary within list atleast five state(key) and capital(value) finally sort the dictionary based on capital name and print result using lambda)
dict=[{'state':'West bengal','capital':'Kolkata'},
        {'state':'Bihar','capital':'Patna'},
        {'state':'Assam','capital':'Dispur'},
        {'state':'Goa','capital':'Panaji'},
        {'state':'Gujrat','capital':'Gandhinagar'}]
sorted_dict=sorted(dict,key=lambda x:x ['capital'])
print(sorted_dict)



