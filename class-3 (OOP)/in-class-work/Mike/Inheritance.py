import math

class Shape(object):
    def __init__(self, shape_type, color):
        self.shape_type = shape_type
        self.color = color
        
    def to_string(self):
        return ("I'm a {} {}.".format(self.color.lower(), self.shape_type.lower()))

class RightTriangle(Shape):
    def __init__(self, color, height, base):
        super(RightTriangle, self).__init__('right triangle', color)
        self.height = height
        self.base = base  
            
    def calc_perimeter(self):
        perimeter = height + self.base + (( self.height ** 2 ) + ( self.base ** 2 )) ** (0.5)
        return ("The perimeter of this {} is {}.".format(self.shape_type.lower(),perimeter))
  
    def calc_area(self):
        area = (self.height * self.base) / 2  
        return ("The area of this {} is {}.".format(self.shape_type.lower(),area))
    
class Circle(Shape):
    def __init__(self, color, radius):
        super(Circle, self).__init__('circle', color)
        self.radius = radius

    def calc_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return ("The perimeter of this {} is {}.".format(self.shape_type.lower(),perimeter))
   
    def calc_area(self):
        area = ( math.pi * self.radius ) ** 2 
        return ("The area of this {} is {}.".format(self.shape_type.lower(),area))
        
class Square(Shape):
    def __init__(self, color, side):
        super(Square, self).__init__('square', color)
        self.side = side
                   
    def calc_perimeter(self):
        perimeter = self.side * 4
        return ("The perimeter of this {} is {}.".format(self.shape_type.lower(),perimeter))
    
    def calc_area(self):
        area = self.side ** 2
        return ("The area of this {} is {}.".format(self.shape_type.lower(),area))

triangle1 = RightTriangle('blue', 5, 4)
square1 = Square('red', 4)
circle1 = Circle('orange', 2)


square1.calculate_perimeter()
