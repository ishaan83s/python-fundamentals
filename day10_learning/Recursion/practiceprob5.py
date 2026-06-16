#Task: Write a recursive function that takes a list and a target value, and returns how many times that target value appears in the list.

def target_value(list,target,index = 0):
    if index == len(list):
        return 0
    
    if (list[index] == target):
        return 1 + target_value(list,target,index+1)
    else:
        return target_value(list,target,index+1)

nums = [1,2,3,4,5,6,7,8,9,10,2]
print(target_value(nums,2))