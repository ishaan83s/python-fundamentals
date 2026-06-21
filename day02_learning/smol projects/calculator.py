#Calculator: Take two numbers from a user, ask them to input an operator (+, -, *, /), and use conditional logic to output the result.

a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
print(" 1 : sum\n 2 : sub\n 3 : multply\n 4 : divide\n 5 : power\n 6 : remainder ")
choice = int(input("Which Operation would you like to choose : "))

if (choice == 1):
    print(a + b)
elif (choice == 2):
    print(a - b)
elif(choice == 3):
    print(a*b)
elif(choice == 4):
    print(a/b)
elif(choice == 5):
    print(a**b)
elif(choice == 6):
    print(a%b)
else :
    print("unknown choice")