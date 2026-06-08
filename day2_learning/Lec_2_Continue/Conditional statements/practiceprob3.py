#WAP to find the greatest of 3 numbers entered by the user

a = float(input("Enter your first number : "))
b = float(input("Enter your second number : "))
c = float(input("Enter your third number : "))
d = float(input("Enter your 4th number : "))

max_num = 0

if(max_num <= a):
    max_num = a
if(max_num <= b):
    max_num = b
if(max_num <= c):
    max_num = c
if(max_num <=d):
    max_num = d

print("Largest number = " , max_num)