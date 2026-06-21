#WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("Enter your physics marks : "))
marks.update({"phy" : x})

y = int(input("Enter your chem marks : "))
marks.update({"chem" : y})

z = int(input("Enter your math marks : "))
marks.update({"math" : z})


print(marks)