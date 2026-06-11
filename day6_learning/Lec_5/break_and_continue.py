#BREAK
i = 1 
while i <= 5:
    print(i)
    if (i==3):
        break
    i = i +1
print("LOOP ENDED\n\n")

#CONTINUE

i = 1
while i <=5:
    if(i == 3):
        i += 1 #if we dont increment here i will forever be 3 as i = i+1 never occured before
        continue #we write the incrementation before continue cuz continue runs the code (basically from while condition) from the top again so its wat it is
        print("PROOF NOTHING RUNS AFTER CONTINUE IN THIS BLOCK")
    print(i)
    i += 1
print("Loop ended")