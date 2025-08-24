'''d={"name":"sampa","age":"19","course":"btech cse"}
print(d)
print(type(d))
print(d['name'])
print(d['age'])
print(d["course"])
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d:
    print(f"{i}:{d[i]}")'''

#frequency count of a string:-
'''name=input("enter your name:")
name=name.lower()
d={}
for i in name:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
# print(d)

for i in d:
    print(f"{i}:{d[i]}")'''

#frequency count of a word:-
'''name=input("enter your string:")
search=input("enter your word:")
print(name)
#split()
c=0
l=name.split()
for i in l:
    if search==i:
        c=c+1
print(f"{search}:{c}")'''

#frequency of each word:-
'''name=input("enter your string:")
d={}
print(name)
#split()
l=name.split()
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    print(f"{i}={d[i]}")'''

'''name=input("enter your string:")
search=input("enter your word:")
print(name)
#split()
l=name.split()
c=l.count(search)
print(f"{search}:{c}")'''

'''l=['s','a','m','p','a']
#join
s=''.join(l)
print(s)'''

#code: input:8BC2A4 output:ABC248(WIPRO)
'''n=input("enter the values=")
alphabet=[]
digit=[]
for i in n:
    if i.isalpha():
        alphabet.append(i)
    else:
        digit.append(i)
print(alphabet)
print(digit)
final_output=sorted(alphabet)+sorted(digit)
s=''.join(final_output)
print(s)'''

'''n=int(input("enter size of list:"))
l=[]
a=0
b=0
for i in range(n):
    v=int(input("enter your list element:"))
    l.append(v)
print("your list=",l) #[1,2,3,4,5,6]
if(len(l)<2):
    print("Maximum pair is not possible")
else:
    a=l[0]
    b=l[1]
    for i in range(0,len(l)):  #i=0,1,2,,3,4,5
        for j  in range(i+1,len(l)): #j=1,2,3,4,5  j=2,3,4,5  j=3,4,5 j=4,5 j=5
            if(l[i]*l[j]>a*b): #1*2>1*2 #1*3>1*2
                a=l[i]   #1
                b=l[j]  #3,4,5
    print((a,b))'''

#target sum pair:-
'''n=int(input("enter tour list range:"))
l=[]
for i in range(n):
    val=int(input("enter your list items:"))
    l.append(val)
target=int(input("enter your target items:"))
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]+l[j]==target):
            print((l[i],l[j]))'''

