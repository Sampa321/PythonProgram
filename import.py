import math
import random
#gcd two number
'''gcd=math.gcd(20,30)
print("GCD=",gcd)
fact=math.factorial(5)
print("factorial=",fact)
print(math.floor(12.4545))
print(math.ceil(12.456565))
print(math.floor(math.pow(2,3)))
print(math.sin(30))
print(math.cos(60))'''

# print(math.pi) #3.14
'''print(random.random()) #0.77(0<x<1)
r2=random.random()
r3=math.floor(r2)
print(r3) #0
r5=random.randint(2,10)
print(r5)
r6=random.randrange(1,6)
print(r6)'''

# l=[2,3,4,6,8,7]
# print(random.choice(l))

'''t=1
choice=int(input("enter your choice:"))
for trial in range(6):#0,1,2,3,4,5
    if(random.choice(l)==choice):# random.choice(l)=2,3,4,6,8,7
        t=t
        break
    else:
        t+=1
    print(f"you won after={t-1} trial")'''

'''l=[1,2,3,4,5,6]
print("Before Suffle your list=",l)
random.shuffle(l)
print("After Suffle your list=",l)'''


r7=math.floor((random.random()*6))+1
print(r7)