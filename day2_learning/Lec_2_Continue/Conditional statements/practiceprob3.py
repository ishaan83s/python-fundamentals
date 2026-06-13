#WAP to find the greatest of 4 numbers entered by the user

a = float(input("Enter your first number : "))
b = float(input("Enter your second number : "))
c = float(input("Enter your third number : "))
d = float(input("Enter your 4th number : "))

max_num = 0

if(max_num <= a):  #WE DONT USE ELIF HERE BECAUSE ELIF DOESNT WORK WHEN IF IS TRUE , BUT IF HOWEVER WORKS IF PAST IF WAS TRUE 
    max_num = a
if(max_num <= b):
    max_num = b
if(max_num <= c):
    max_num = c
if(max_num <=d):
    max_num = d

print("Largest number = " , max_num)