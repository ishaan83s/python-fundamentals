class Car:

    def __init__(self,type): #THIS IS A CONSTRUCTOR , it is also a method
        self.type = type
    
    def lights(self,light):
        self.light = light

    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    brand = "toyota"
    def __init__(self, name , type , light):
        super().__init__(type)
        super().lights(light)
        super().start() #IF WE WANT TO START AS SOON AS OBJECT IS CREATED THEN WE CAN CALL THE METHOD OF SUPER CLASS
        self.name = name

        




car1 = ToyotaCar("Fortunaaaar","diesel","fog")
print(car1.name)
print(car1.type)
print(car1.light)

#SO BASICALLY THE SUPER IS USED TO CALL ANY METHOD (FUNCTION) THAT IS PRESENT IN PARENT CLASS
#first the "type" argument that we needed , we called the __init__ method 
#__init__ is used for constructor but its bigger picture is that its also a method
#Therefore , super().__init__(type)

#FOR THE SECOND ARGUMENT THAT WAS NEEDED "LIGHT"
#we call the LIGHTS method(function) , i.e present in parent class
#Therefore , super().lights(light)