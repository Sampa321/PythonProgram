#print uncommon word in two string.
l1=[]
l2=[]
uncommon_word=[]
str1=input("enter first string:")
str2=input("enter second string:")
l1=str1.split()
l2=str2.split()
for i in l1:
    if i not in l2:
        uncommon_word.append(i)
for i in l2:
  if i not in l1:
      uncommon_word.append(i)
print(uncommon_word)