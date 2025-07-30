#check character is present in a string.
'''name=input("enter the string")
count=0
a=input("Enter the ch:")
for i in name:
    if a==i:
        count=1
if count==1:
    print("Yes Present")
else:
    print("Not Present")'''
 

#wap frequency of each character.
str=input("enter the string:")
dic={}
for i in str:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
