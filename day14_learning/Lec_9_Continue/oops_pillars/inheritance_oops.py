class Car:
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car): #SINGLE INHERITANCE FROM PARENT CLASS CAR
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar): #MULTILEVEL INHERITENCE , inherit from child class car (for this its parent class)
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()