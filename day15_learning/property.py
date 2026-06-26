#"@property" is a decorator on any method to use that method as a property . property aka attribute

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"

stu1 = Student(99,88,97)
print(stu1.percentage)