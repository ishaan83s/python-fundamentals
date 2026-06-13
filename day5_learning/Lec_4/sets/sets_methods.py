s = set()
s.add(10)
s.add(20)
s.add("ishaan")
s.add(2010)
s.add("Jay")
print(s)


s.remove("Jay") #removes particular element but if there is no element as such in the set then it gives error
print(s)

s.pop() #pops any random element existing in set
print(s)

s.clear() #empties the set
print(s)