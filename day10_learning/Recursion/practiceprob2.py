#Write a recursive function to print all elements in a list 
#Hint : use list and index as parameters

def prlistele(list,index = 0):
    if index == len(list):
        return
    else:
        print(list[index])
        prlistele(list,index+1)


numbers = [12,3,4,5,5,2,1]
prlistele(numbers)