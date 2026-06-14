#WAF to print odd if num is odd , and even if num is even

def odd_even(n):
    if n%2 == 0:
        print("EVEN")
    else:
        print("ODD")

odd_even(int(input("Enter your number to check : ")))