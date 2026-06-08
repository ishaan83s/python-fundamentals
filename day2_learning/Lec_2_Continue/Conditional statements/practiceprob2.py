#WAP to find the greatest of 3 numbers entered by the user

x = float(input("Enter your first number : "))
y = float(input("Enter your second number : "))
z = float(input("Enter your third number : "))

if (x>y and x>z):
    print("first is greatest number" , x)
elif(y>z):
    print("second is greatest number" , y)
else:
    print("third is greatest number" , z)