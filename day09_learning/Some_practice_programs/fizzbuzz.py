#So basically the objective is to write a program that prints integers from 1 to n, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz"

n = int(input("Enter your number : "))

for i in range(n+1):
    if i%3 == 0 and i%5 != 0:
        print(i,"FIZZ")
    elif i%5 == 0 and i%3 != 0:
        print(i,"BUZZ")
    elif i%3== 0 and i%5 == 0:
        print(i,"FIZZ BUZZ")
    else:
        print(i)