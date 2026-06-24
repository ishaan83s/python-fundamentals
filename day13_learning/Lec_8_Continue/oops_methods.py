class Student:
    college_name = "TCET"
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    def welcome(self):
        print("welcome student :",self.name)
    
    def get_marks(self):
        return self.marks
    
s1 = Student("Karan", 67) #KARAN AND 67 ARE INSTANCE ATTRIBUTE
print(s1.college_name) #CLASS ATTRIBUTE
s1.welcome()
print(s1.get_marks())