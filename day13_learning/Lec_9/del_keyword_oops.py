class Student:
    def __init__(self,name):
        self.name = name
    
s1 = Student("Vivi")

print(s1.name) #PRINTS "Vivi"
del s1.name #DELETES THE OBJECT PROPERTY I.E NAME
# print(s1.name) #Gives an error as s1.name no longer exists

print(s1) #PRINTS "<__main__.Student object at 0x10489de80>"
del s1
print(s1) #GIVES AN ERROR AS s1 no longer exists