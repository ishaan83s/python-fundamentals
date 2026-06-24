class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True 
        print("Car Started...")

car1 = Car()
car1.start()

#TO PERFORM START WE DONT SEE THE WORKING OF THE CLASS. 
#THIS IS CALLED ABSTRACTION , WE ONLY LET USER SEE WHATS NECESSARY