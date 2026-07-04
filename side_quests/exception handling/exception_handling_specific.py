try:
    a = [6,3]
    print(f"choose index to be printed from :{a}")
    x = int(input("Enter your number"))
    print(a[x])
except ValueError: #If we enter any string it gives value error
    print("Value entered is not a valid input")

except IndexError: #If we enter an invalid index it gives index error
    print("Index Error : index doesnt exist")