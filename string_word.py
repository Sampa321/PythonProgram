#print string number in colum wise.
name=input("enter the string:")
for i in name:
 print(i)

 #Question-5(Find non-repeating characters in a string)
str=input("enter the string:")
for i in str:
    if str.count(i)==1:
        print(i)
