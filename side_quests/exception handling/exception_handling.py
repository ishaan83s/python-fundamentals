x = input("Enter a number :") #purposely didnt take x as int
print(f"Multiplication table of {x} is : ")

try:
    for i in range(1,11):
        print(f"{int(x)} X {i} = {int(x)*i}") #if we give input as string it gives error 
except Exception as e:
    print(e)

#THIS PRINTS ERROR IF WE USE A STRING BUT THE PROGRAM STILL RUNS TILL END
#invalid literal for int() with base 10: 'Ishaan'
print("AND THESE ARE SOME IMPORTANT LINES OF CODE")
print("End of program")