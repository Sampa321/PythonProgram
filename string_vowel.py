#count vowel and consonant in a string.
name=input("enter the string:")
v_count=0
c_count=0
for i in name:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
      v_count+=1
    else:
      c_count+=1
print(f"No_of_vowel={v_count} No_of_consonant={c_count}")