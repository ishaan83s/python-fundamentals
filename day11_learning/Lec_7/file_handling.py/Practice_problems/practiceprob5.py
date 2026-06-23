#FROM A FILE CONTAINING NUMBERS SEPERATED BY COMMA , PRINT THE COUNT OF EVEN NUMBERS

with open("/Users/ishaan/Desktop/python-learning/day11_learning/Lec_7/file_handling.py/Practice_problems/numbers.txt","r") as f :
    data = f.read() + ","
    num = ""
    for i in range(len(data)):
        if data[i] == ",":
            if int(num)%2 != 0:
                continue
            else:
                print(int(num))
            num = ""
        else:
            num += data[i]

