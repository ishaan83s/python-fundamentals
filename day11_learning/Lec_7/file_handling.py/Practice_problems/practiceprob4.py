#WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found.
def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("/Users/ishaan/Desktop/python-learning/day11_learning/Lec_7/file_handling.py/Practice_problems/practice1.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            else:
                line_no += 1
        
    return -1

check_for_line()