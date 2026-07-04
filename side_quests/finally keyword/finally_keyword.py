def func1():
    try:
        l = [1,2,3,4,5,6]
        i = int(input("Type your index :"))
        print(l[i])
        return 1

    except: #ONLY RUNS WHEN ERROR
        print("Some error occured")
        return 0 

    finally:
        print("I am finally clause , I am always executed")

x = func1()
print(x) #print 0 if error occured and 1 if no error


#WHY NOT JUST USE :
#print("I am always executed") 
#it will also run everytime we run the program. 
#so basically when we wrap this in a function then after returning the compiler never reachers the print part
#therefore its never printed but finally block is printed everytime
