#Count no of letters,digits,special characters in a string.
name=input("enter the string:")
letter_count=0
digit_count=0
spe_char=0
for i in name:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        letter_count+=1
    elif (i>='0' and i<='9'):
       digit_count+=1
    else:
        spe_char+=1
print(f"numbers_letters={letter_count} digits={digit_count} special_character={spe_char}")
 