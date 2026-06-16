#Task: Write a recursive function to print all elements in a list in reverse order (from the last element to the first element).

def print_list(lis,index = None):
    if index == None:
        index = len(lis)-1

    if (index <0):
        return
    else:
        print(lis[index])
        print_list(lis,index-1)

nums = [1,2,3,4,5,6,7,8,9,10]

print_list(nums)