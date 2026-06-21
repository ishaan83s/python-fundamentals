#WAP to check if a list contains a palindrome of elements. 
list0 = [1,2,3,2,1] 
list1 = list0.copy() #list1 becomes 1,2,3,2,1
list1.reverse() #list1 becomes 1,2,3,2,1

if (list1 == list0):
    print("list contains a palindrome of elements")
else:
    print("list doesnt contain palindrome of elements")