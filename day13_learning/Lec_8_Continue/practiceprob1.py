#CREATE STUDENT CLASS THAT TAKES NAME & MARKS OF 3 SUBJECTS AS ARGUMENT IN CONSTRUCTOR.
#THEN CREATE A METHOD TO PRINT AVERAGE

class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name 
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def average(self):
        sum = self.marks1+self.marks2+self.marks3 
        print(sum/3)

stu1 = Student("COCO",87,67,99)

stu1.average()