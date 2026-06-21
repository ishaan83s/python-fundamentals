#WAF that replace all occurences of "Python" with "java" in practice1.txt

with open("/Users/ishaan/Desktop/python-learning/day11_learning/Lec_7/file_handling.py/Practice_problems/practice1.txt","r+") as f:

    stree= str(f.read())
    print(stree)
    print(type(stree))

    stree2 = stree.replace("Python","Java")
    
with open("/Users/ishaan/Desktop/python-learning/day11_learning/Lec_7/file_handling.py/Practice_problems/practice1.txt","w") as f: 
    f.write(stree2)