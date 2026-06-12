#WAP to find the factorial of first n number. (using for)

n = int(input("Enter your number"))
fact = 1

for i in range(1,n+1,1):
    fact = fact * i

print(fact)