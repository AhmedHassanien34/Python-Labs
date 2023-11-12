#Lab1   
'''
Number = int(input("Enter your Number : "))
print(f"{Number:,}")
'''

#Lab2
'''
number = "512345678"
start = len(number)%3
no_of_parts = len(number)//3
result = number[:start]
for i in range(no_of_parts):
    next_part = number[start:start+3]
    if start == 0:
        result = next_part
    else:
        result = result + "," + next_part
    start = start + 3
print(result)
'''

#Lab3 ( "rhinoceros" to rHiNoCeRoS )
'''
original = "rhinoceros"
modified =""
for i in range(len(original)):
    if i%2 == 0:
        modified += original[i]
    else:
        modified += original[i].upper()
print(modified)
'''

#Lab4
'''
User_Name = input("Enter your Email : ").strip()
Password =  input("Enter your Password : ")

if User_Name.lower() == "admin" and Password == "Admin":
    print("Valid")
else:
    print("Invalid")
'''

#Lab5
'''
Name = input("Enter your Name : ").strip()
Age =  input("Enter your Age : ")

if  Age.isdigit():
    print("Age is Valid")
else:
    print("Age is Invalid, Enter Valid Age")
'''
#Lab6 -> 3 Answers
'''
email = "Ahmedtorres2000@gmail.com"
splited_email = email.split("@")
first_part = splited_email[0]
domain_name = splited_email[1]
new = ""
new += first_part[:2]
for i in range(2,len(first_part)):
    new += "*"
print(f"{new}@{domain_name}")
'''
'''
email = "Ahmedtorres2000@gmail.com"
splited_email = email.split("@")
first_part = splited_email[0]
domain_name = splited_email[1]
stared_email_name = first_part[:2] + "*"*(len(first_part)-2)
print(stared_email_name +"@"+domain_name)
'''
'''
email = "Ahmedtorres2000@gmail.com"
formated_email = email.replace(email[2:email.index("@"):], '*'*(email.index("@")-2))
print(formated_email)
'''

#Lab7
'''
password = "Hello1234"
num_of_upper_letters   = 0
num_of_lower_letters   = 0
num_of_digits_letters  = 0
num_of_special_letters = 0

for letter in password:
    if letter.isupper():
        num_of_upper_letters   += 1
    elif letter.islower():
        num_of_lower_letters   += 1
    elif letter.isdigit():
        num_of_digits_letters  += 1
    elif letter in "!@#$%^&*()_+=":
        num_of_special_letters += 1

error_flag = False
if num_of_upper_letters == 0 :
    error_flag = True
    print("Password must contain at least 1 upper case")
if num_of_lower_letters == 0 :
    error_flag = True
    print("Password must contain at least 1 lower case")
if num_of_digits_letters == 0 :
    error_flag = True
    print("Password must contain at least 1 digit")   

if error_flag == False:
    print("Valid")
'''












