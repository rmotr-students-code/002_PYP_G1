# create a "Shape" abstract class, and implement 3 classes that inherit from it: Triangle, Circle, Square. 
# Each class has to be able to perform the following method:
# to_string:  # returns a string explaining the shape type and color
# calculate_area:  # returns the shape area depending on the shape type
# calculate_perimeter:  # returns the shape perimiter depending on the shape type

from math import pi
from math import sqrt

class Shape(object):
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
        
    def to_string(self):
        return "This object is a {} {}" .format(self.color,self.shape)
 
    def calculate_area(self):
        return "The {} has an area equal to {} units" .format(self.shape, self.area)
        
    def calculate_perimiter(self):
        return "The {} has a perimiter equal to {} units" .format(self.shape, self.perimiter)
        
class Triangle(Shape):
    #assuming all triangles are right angled
    def __init__(self, color, height, base, shape_type="Triangle"):
        super(Triangle, self).__init__(color, shape_type)
        self.area = (height * base) / 2
        self.hypotenuse = sqrt((height**2)+(base**2))
        self.perimiter = self.hypotenuse + height + base
    
class Circle(Shape):
    def __init__(self, color, radius, shape_type="Circle"):
        super(Circle, self).__init__(color, shape_type)
        self.area = pi*(radius**2)
        self.perimiter = 2*pi*radius
        
class Square(Shape):
    def __init__(self, color, segment_len, shape_type="Square"):
        super(Square, self).__init__(color,shape_type)
        self.area = segment_len*segment_len
        self.perimiter = segment_len*4

        
triangle = Triangle("blue", 5, 12)
circle = Circle("red", 10)
square = Square("orange", 5)

print square.calculate_area()
#print circle.calculate_area()
#print triangle.calculate_perimiter()        
        
        
    
    