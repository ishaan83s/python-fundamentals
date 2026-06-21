#SEARCH IF THE WORD "learning" exists in the file or not

with open("/Users/ishaan/Desktop/python-learning/day11_learning/Lec_7/file_handling.py/Practice_problems/practice1.txt","r") as f:
    stree = f.read()
    if "learning" in stree.lower():
        print("exists")
    else:
        print("Doesnt exists")

    
    # word = "learning"
    # if (stree.lower().find(word) != -1):
    #     print("found")
    # else:
    #     print("not found")