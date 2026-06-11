#Search for a number x in this tuple using loop :
#(1,4,9,16,25,36,49,64,81,100)

tup = (1,4,9,16,25,36,49,64,81,100)
find = int(input("Enter the number you wanna find"))
i = 0

while i < len(tup):
    if(tup[i] == find):
        print("your number is at index", i)
    else:
        print("finding...")
    i = i + 1

#tup.index