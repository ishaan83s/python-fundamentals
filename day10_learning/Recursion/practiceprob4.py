#Write a recursive function that takes a list of numbers and returns the total sum of all the numbers in that list.

def sumlist(list,index=0):
    if (index == len(list)):
        return 0
    else:
        return list[index] + sumlist(list,index+1)

nums = [1,2,3,4,5,6,7,8,9,10]
print(sumlist(nums))