#Dictionary is a data structure store key and value.
'''MY_dict={'Name':'SAMPA NAYAK','Depertment':'Btech cse','Group':'B','Roll No':'313','College Name':'SVU'}
print(MY_dict)   #{'Name': 'SAMPA NAYAK', 'Depertment': 'Btech cse', 'Group': 'B', 'Roll No': '313', 'College Name': 'SVU'}
print(MY_dict.values())  #dict_values(['SAMPA NAYAK', 'Btech cse', 'B', '313', 'SVU'])
print(MY_dict.keys())
for i in MY_dict:
    print(i)
    print(MY_dict[i])
print(MY_dict['Name'])
print(MY_dict['Depertment'])
print(MY_dict['Group'])
print(MY_dict["Roll No"])
print(MY_dict['College Name'])'''

#CREATE A DICTIONARY{'STATE':'CAPITAL'} ATLEAST FIVE STATE AND CAPITAL AND PRINT STATE AND CAPITAL USING LOOP:
'''my_dict={'West Bengal':'Kolkata','Bihar':'Patna','Assam':'Dispur','Rajasthan':'Jaipur','Madhya Pradesh':'Bhopal'}
for i in my_dict:
    print(i,"=",my_dict[i])'''

my_dic={'NAME':'SAMPA NAYAK','GROUP':'B','STREAM':'B TECH CSE',"ROLL NO":'313','COLLEGE NAME':'SVU'}
for i in my_dic:
    print(i)
for i in my_dic:
    print(my_dic[i])