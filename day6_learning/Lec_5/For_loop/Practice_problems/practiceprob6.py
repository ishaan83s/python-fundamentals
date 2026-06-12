#WAP to find the sum of first n natural numbers . (using while)

n = int(input("Enter value of n : "))
i = 1
sum = 0 


while i <= n:
    sum = sum+i
    i = i + 1 
print(sum)