#Define a Employee class with attribute role , department and salary .
#This class also has a showDetails() method.
#Create an Engineer class that inherits properties from the Employee 
# and has additional attributes name & age 

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("role = ", self.role ,"\ndept = ", self.dept , "\nsalary = ", self.salary)

class Engineer(Employee):
    def __init__(self,role,dept,salary,name,age):
        super().__init__(role,dept,salary)
        self.name = name 
        self.age = age


engg1 = Engineer("SWE","DEV",4000000,"Ishaan",23)
print(engg1.name , engg1.age , engg1.role , engg1.dept , engg1.salary)
engg1.showDetails()