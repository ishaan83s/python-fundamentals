import random

secret = random.randint(1,10)

num_guess = 0
while True:
    var = int(input("Enter number from 1-10 : "))

    if num_guess ==10:
        break
    if var == secret:
        print("You Got the correct number....")
        break

    elif var > 10:
        print("Your guess number is not in the actual range...")

    elif var < secret:
        print("Try again , Number is greater than your guess...")
        num_guess += 1

    elif var > secret:
        print("Try again , Number is smaller than your guess...")
        num_guess += 1

print("----GAME OVER----")