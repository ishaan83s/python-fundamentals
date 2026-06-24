class Student:
    def __init__(self,name,id,passw):
        self.name = name
        self.id = id
        self.__passw = passw

    def getpassw(self):
        print(self.__passw)

stu1 = Student("ayush",1,"sumo")

# print(stu1.__passw) # GIVES ERROR BECOZ OUTSIDE OF CLASS

#LETS CALL GET PASSW

stu1.getpassw() #THIS PRINTS "self.__passw" because this method
#is itself inside the class and has access to it
