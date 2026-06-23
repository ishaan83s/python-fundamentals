class Student:
    def __init__(self,name,marks): #constructor cannot work without a self argument...we can add multiple argument after self
        self.name = name #THE SELF POINTS TO s1 (or any other object created from this class)
        self.marks = marks
        #HERE THE NAME OF s1 will BECOME FULLNAME
        print("Adding new student in database...")

s1 = Student("PETER",67) #we pass "PETER " as a value of fullname that is assigned for s1
print(s1.name , s1.marks)

s2 = Student("Arjun",67)
print(s2.name,s2.marks)