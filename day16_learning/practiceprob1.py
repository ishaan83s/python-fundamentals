#Define a Circle class to create a cricle with radius r using the constructor. Define the Area() 
#Method of the class which calculates the the area of the circle.
#Define a Parimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        calc1 = (22/7) * (self.radius  **2)
        return calc1
    
    def perimeter(self):
        calc2 = 2 * (22/7) * self.radius
        return calc2
    
circle1 = Circle(21)
print(circle1.radius)
print(circle1.area())
print(circle1.perimeter())