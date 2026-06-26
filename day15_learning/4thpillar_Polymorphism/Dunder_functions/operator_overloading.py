#HERE WE ARE MAKING A CLASS FOR CMPLX NUMBERS OPERATIONS BY USING OPERATORS AS "+","-"
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def __add__(self, num2): #__add__ this is dundder function for "+" 
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal , newImg)
    
    def __sub__(self, num2): # __sub__ this is dundder function for "-" 
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal , newImg)

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

num1 = Complex(13,17)
num2 = Complex(4,6)

num3 = num1 + num2 
num3.showNumber()

#MORE DUNDDER FUNCTIONS:

# a+b #addition = a.__add__(b)
# a-b #subtraction = a.__sub__(b)
# a*b #multiplication = a.__mul____(b)
# a/b #division = a.__truediv____(b)
# a%b #modulo = a.__mod____(b)