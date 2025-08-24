#WAP count uppercase,lowercase,number and special character.
Email=input("enter the email:")
UC=0
LC=0 #13
NO=0 #3
SC=0 #2
for i in Email:
    if(i>='A' and i<='Z'):
        UC+=1
    elif(i>='a' and i<='z'):
        LC+=1
    elif(i>='0' and i<='9'):
        NO+=1
    else:
        SC+=1
print(f"No of uppercase={UC} No of LOWercase={LC} No of number={NO} No of special char={SC}")
