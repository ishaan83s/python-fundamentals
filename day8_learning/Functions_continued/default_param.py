def cal_prod(a = 1 , b = 1):
    print(a*b)
    return a*b

cal_prod() #this will print 1

#we give default values from the end 
#for eg :
def cal_sum (a,b=0):
    print(a+b)
    return a+b

cal_sum(3)