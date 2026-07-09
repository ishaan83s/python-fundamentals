fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits): #THIS MAPS EACH ELEMENT WITH ITS INDEX SAVING MORE TIME MANUALLY GETTING THE INDEX OF GETTING THE 
#VALUE OF I IN RANGE TYPE OF THING
    print(f"Index: {index} | Fruit: {fruit}")

items = ["Gold Medal", "Silver Medal", "Bronze Medal"]



# Start counting from 1 instead of 0
for rank, item in enumerate(items, start=1):
    print(f"{rank}. {item}")