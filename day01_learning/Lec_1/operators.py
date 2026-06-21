#arithmetic operators 
a = 5
b=2

sum = a + b
diff = a -b 

print(sum,diff)
print(a+b) #sum
print(a-b) #subtract
print(a*b) #multipy
print(a/b) #divide
print(a**b) #power
print(a%b) #remainder 

#relational operators
a = 50
b = 20
print(a,b)
print(a==b) #equal to operator (its not a = b because that is an assignment operator)
print(a!=b) #not equal to operator
print(a>b) #greater than operator
print(a<b) #less than operator
print(a>=b) #greater than or equal to operator
print(a<=b) #less than or equal to operator

#assignment operators
num=10
num = num +10 
print(num)

num += 10 #this is the same as num = num + 10
print(num)

num -= 10 #this is the same as num = num - 10
print(num)

num *= 10 #this is the same as num = num * 10
print(num)

num /= 10 #this is same as num = num/10
print(num)

num **= 10 #this is the same as num = num ** 10
print(num)

num %= 10 #this is the same as num = num % 10
print(num)

#logical operators
m = True
n = True
o = False
print (not m and o)
print(not m or n)
print (not m)
print (m and n)
print (m or o)

m = 5
n= 10
o = 15

print( (m==n) or (m>n)) # false or false = false
print( (m==n) or (m<o)) # false or true = true 