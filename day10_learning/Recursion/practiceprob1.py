#Write a recursive function to calculate the sum of first n natural numbers.

def natural(n):
    if (n==0):
        return 0
    else:
        return n + natural(n-1)
    
print(natural(3))