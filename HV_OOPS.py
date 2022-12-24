class Shape():
      
    # Constructor
    def __init__(self,side,side1):
        self.side = side
        self.side1 = side1
          
    
    def area(self):
        print(f"Area is = {self.side1*self.side} mm^2")
          
# Defining child class
class Square(Shape):
      
    # Constructor
    def __init__(self,value):
        self.value = value
          
    # Child's area method
    def area(self):
        print(f"Area is = {self.value*self.value} mm^2")
          
# Defining child class
class Circle(Shape):
      
    # Constructor
    def __init__(self,rad):
        self.rad = rad
          
    # Child's area method
    def area(self):
         print(f"Area is = {self.rad*self.rad*3.14} mm^2")
          
# Driver's code
rectangle = Shape(10,20)
square = Square(30)
cicle = Circle(30)
  
rectangle.area()
square.area()
cicle.area()
