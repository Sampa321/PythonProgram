#count search no of character in a string.
name=input("enter your name:")
count=0
search_char="a"
for i in name:
    if search_char==i:
        count+=1
print(count)