p = 5000
target = 7500
t = 7 
n = 2
r = 0.065

A = p * (1+r/n)**(n*t)

if (A > target):
    print("You can buy the boat")
else :
    rem = round(target - A,2)
    print("You need ", rem ," to but the boat")


