#Lab1
'''
Age = input("Enter your Age :")

if (Age >= 10 and Age < 25):
    print("You are Young")
elif Age > 25 :
    print("You are old")
else :
    print("you are kid")

'''

#Lab2
'''
Age = input("Enter your Age : ")
Age = int(Age)

if Age < 11 :
    print("Not Eligible")
elif 10 < Age < 20 :
    print("2$ for ticket")
elif 19 < Age < 61:
    print("10$ for ticket")
else :
    print("7$ for ticket")

'''

#Lab3
'''
Speed = input("Enter your Speed :")
Speed = int(Speed)
Birthday =input("it is your birthday Y/N :")

if (Birthday == "Y"):
    Speed -= 5

if Speed < 61 :
    print("No Ticket")
elif Speed < 81:
    print("Small Ticket")
else:
    print("Big Ticket")

'''

#Lab4
'''
for i in range(0,21,1):
    if i%2==0:
        print(i)    
'''

#Lab5
'''
#Lab5 /*Perfect Number*/
Number = int(input("Please Enter Number : "))
Sum = 0
for i in range(1,Number//2 +1):
    if Number % i == 0:
        Sum += i

if Sum   == Number:
    print ("Number is Perfect")
else:
    print("Number is not Perfect")
'''
#Lab6
'''
num_of_digits = int(input("Pls Enter num of digits :"))
int("2"*num_of_digits)

final = 0 
for i in range (1,num_of_digits+1):
    final += int("2"*i) 

print(final)
'''

#Lab7
'''
S = "This dog runs faster than the other dog dude dog"
word = ""
counts = 0
for letter in S:
    if letter != " ":
        word = word + letter
    else:
        if word == "dog":
            counts = counts + 1
        word = ""
if word == "dog":
    counts = counts + 1
print(counts)
'''
'''
#OR
S = "This dog runs faster than the other dog dude dog"
counts = 0
for i in range(len(S)):
    if S[i:i+3] == "dog":
        counts = counts + 1
print(counts)
'''

#Lab8
'''
User_Name = input("Enter your Email : ")
Password =  input("Enter your Password : ")

if User_Name.lower() == "admin" and Password == "Admin":
    print("Valid")
else:
    print("Invalid")
'''














