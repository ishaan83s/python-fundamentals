# # I WILL TRY TO DO THIS PROGRAM BY USING SET , [huh we cant generate the number from set]

# set0 = {1,2,3,4,5,6,7,8,9,10}

# while len(set0) >=0:
#     var=set0.pop()
#     g_num = int(input("Guess a number from 1-10 : "))

#     if var == g_num:
#         print("\nYou guessed it right")
#         break
#     else:
#         print("\nGuess again. The number was : ",var)
#         set0.add(var)

import random
secret = 7

#Or 
# secret = random.randint(1,10)

var = int(input("Enter number from 1-10 : "))

if var == secret:
    print("You Got the correct number....")
elif var > 10:
    print("Your guess number is not in the actual range...")
elif var < secret:
    print("Try again , Number is greater than your guess...")
elif var > secret:
    print("Try again , Number is smaller than your guess...")
