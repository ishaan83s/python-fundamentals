#WE CAN OPEN FILE LIKE DIS 

with open("/Users/ishaan/Desktop/python-learning/day11_learning/Lec_7/file_handling.py/demo.txt","r") as f:
    data = f.read()
    print(data)

with open("/Users/ishaan/Desktop/python-learning/day11_learning/Lec_7/file_handling.py/demo.txt","w") as f:
    data = f.write("nu uh")
    print(data)