#Search for a number x in this tuple using loop
num = int(input("Enter number that you wanna find"))
find = [1,4,9,16,25,36,49,64,81,100,25]
index = 0 
for i in find:
    if (i==num):
        print(num,"FOUND" , index)
    index +=1
else:
    print("NUMBER NOT FOUND")