str1 = "Is this peak? Yes \nYes but in Yellow" #THIS IS /n NEW LINE
str2 = "Is this peak? Yes \tYes but in Yellow" #THIS IS /t TAB 
print(str1)
print(str2)

#CONCATINATION 

a = "\nViv"
len1 = len(a)
print(len1)
b = "aan"
len2 = len(b)
print(len2)
len3 = len(a+ " " +b)
print(len3)
print(a+b) #or str_final = a + b then print str_final
str = "SUWOOP big_blat"
ch = str[10]
print(ch) #10th index is underscores
print(str[6]) #6th index is space 
print(str[:8]) # this is print elemnts of allindexes from 0-7 ,8th excluded
print(str[6:]) #this is print elements after index 6 and 6 included