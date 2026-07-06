#__str__ METHOD IS USED TO REPRESENT OBJECT OF THAT CLASS IN HUMAN READABLE WAY (HUMAN READABLE STR)
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    def __str__(self):
        return f"{self.name} ({self.grade})"
    
mary = Student("Mary","A+")
print(mary) 

mary_string = str(mary) #ONE MORE WAY TO DO WITHOUT STR METHOD 
print(mary_string)

#if str method didnt exist it wouldve printed "<__main__.Student object at 0x102456120>"
#its not human readable 
