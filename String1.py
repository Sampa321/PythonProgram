'''name="sampa"
print(name)  #sampa
#strint slicing'''
'''print(name[2])  #m
print(name[:2])  #sa
print(name[1:4])  #amp
print(name[2:])  #mpa'''
'''print(type(name))  #str
print(len(name))   #5
size=len(name)
for i in range(size):
    print(name[i])

for i in name:
    print(i)'''

#lower() and upper()
'''name="Mamon"
name1=name.upper()
name2=name.lower()
print(name)  #Mamon
print(name1)  #MAMON
print(name2)  #mamon'''

#remove odd position character i a string.
'''result=""
str=input("enter the string:")
for i in range(len(str)):
    if i%2==0:
        result+=str[i]
print(result)'''

#remove even position character i a string.
'''result=""
str=input("enter the string:")
for i in range(len(str)):
    if i%2==1:
        result+=str[i]
print(result)
'''
#check a string containt how many digit,alphabet,special character.
'''email=input("enter the string:")
email1=email.lower()
digit=0
alphabet=0
special_character=0
for i in email1:
    if(i>='a' and i<='z'):
        alphabet+=1
    elif(i>='0' and i<='9'):
        digit+=1
    else:
        special_character+=1
print(f"digit={digit} alphabet={alphabet} special character={special_character}")'''

n=int(input("enter a number:"))#8
s=""
while(n!=0):
    r=n%10  #8,4,2,1
    s=s+str(r) #" "+"8"+"4"+"2"+"1"
    n=n//2 #4,2,1
print(s) #8421
for i in reversed(s): 
    print(i) 

'''month=input("Enter any month:")
m=month.lower()
if(m=="march" or m=="april" or m=="may"):
    print("spring")
elif(m=="june" or m=="july" or m=="august"):
    print("summer")
elif(m=="september" or m=="october" or m=="november"):
    print("Autumn")
elif(m=="december" or m=="january" or m=="february"):
    print("Winter")
else:
    print("wrong choose")'''

#print reverse string using inbuild method.
# st=input("enter your str:")
# reverse_string=st[::-1]
# print(reverse_string)
