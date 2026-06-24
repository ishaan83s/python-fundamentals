#STATIC METHOD : METHODS THAT DONT USE THE SELF PARAMETER
#THIS METHOD WORKS AT CLASS LEVEL RATHER THAN OBJECT LEVEL

class Student:
    @staticmethod #THIS IS A DECORATOR
    def college(): #THIS METHOD WORKS WITHOUT SELF OR ANY PARAMETER, IF DIDNT USE @staticmethod it will give error
        print("TCET")

stud1 = Student()
stud1.college()

#Decorator : Decorator allows us to wrap another function in order to extend the behaviour of the wrapped function without permanently modifying it.