list = [2,1,3]

list.append(4) #adds element to the end of the list #this changes the list itself
print(list)

list.sort() #sorts in ascending order #this changes the list itself
print(list)

list.sort(reverse=True) #sorts in decending order #this changes the list itself
print(list)

list.reverse() #reverses the list
print(list)

list.insert(1,5) #inserts the element without replacing the og element but pushing the element og index+1 and so on with next elements
print(list)

list.remove(1) #remove the first occurence of the element i.e 1
print(list)

list.pop(2) #2 is the index #we pop the element on index 2 here
print(list)

