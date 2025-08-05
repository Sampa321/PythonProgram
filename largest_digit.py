#largest digit in a given numbers.
num=int(input("enter the number:"))
s1=(str)(num)
s2=list(s1)
s2.sort()
print(s2)
print(int(s2[len(s2)-1]))