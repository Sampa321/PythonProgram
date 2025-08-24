'''print the pattern:
*
**
***
****
*****'''
'''n=int(input("enter the number:"))
for i in range(0,n+1):
    for j in range(0,i+1):
        print("*",end="")
    print()'''

'''print the pattern:
* * * 
* * *
* * *      #n=3'''
'''n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()'''

'''print the pattern:
1
12    #n=3
123'''
'''n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''


'''print the pattern:
1
22   #n=3
333'''
''''n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()'''

'''print the pattern
1 
2 3
4 5 6       #a=5,n=1
7 8 9 10
11 12 13 14 15'''
'''a=int(input("enter the number:"))
n=int(input("enter the number:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print()'''

'''Question-(print the pattern):
*       
* *     
* * *   
* * * *      #n=4
* * *   
* *
*'''
'''n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
            print("*",end=" ")
    print()
for i in range(1,n):
    for j in range(0,n-i):
        print("*",end=" ")
    print()'''


'''
print the pattern:
A
B B
C C C
D D D D
E E E E E
'''
'''n=int(input("Enter the number of >65:"))
for i in range(65,n+1):
    for j in range(65,i+1):
        print((chr(i)),end=" ")
    print()'''
    

'''
print the pattern:
a 
b b
c c c
d d d d
e e e e e
f f f f f f
'''

n=int(input("Enter the number of >97:"))
for i in range(97,n+1):
    for j in range(97,i+1):
        print((chr(i)),end=" ")
    print()