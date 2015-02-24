"""# create a "Shape" abstract class, and implement 3 classes that inherit from it: Triangle, Circle, Square. 
Each class has to be able to perform the following method:
to_string:  # returns a string explaining the shape type and color
calculate_area:  # returns the shape area depending on the shape type
calculate_perimeter:  # returns the shape perimiter depending on the shape type
"""
import math

class Shape(object):
    def __init__(self, colour):
        self.colour = colour
        
    def to_string(self):
        return 'This is a {colour} {shape}'.format(colour=self.colour, shape=
            self.shape_type)
    
    def print_area_and_perimeter(self):
        print 'The {colour} {shape} has an area of {area} and perimeter {perimeter}'\
            .format(colour=self.colour, shape=self.shape_type, area=
            self.calculate_area(), perimeter=self.calculate_perimeter())
        
            
class Triangle(Shape):
    def __init__(self, colour, side1, side2, side3):
        super(Triangle, self).__init__(colour)
        self.a = float(side1)
        self.b = float(side2)
        self.c = float(side3)
        self.shape_type = 'Triangle'
    
    def calculate_area(self):
        if self.a != self.b and self.b != self.c and self.a != self.c:
            s = (self.a + self.b + self.c) / 2
            self.shape_type = 'Scalence Triangle'
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            
        elif self.a == self.b and self.a == self.c and self.b == self.c:
            self.shape_type = 'Equilateral Triangle'
            return math.sqrt(3) / 4 * self.a ** 2
            
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            self.shape_type = 'Isosceles Triangle'
            if self.a == self.b:
                return 0.5 * self.c ** 2 * math.sqrt((self.b ** 2 / self.c ** 2) - (1 / 4))
            elif self.b == self.c:
                return 0.5 * self.a ** 2 * math.sqrt((self.b ** 2 / self.a ** 2) - (1 / 4))
            else:
                return 0.5 * self.b ** 2 * math.sqrt((self.a ** 2 / self.b ** 2) - (1 / 4))
        
    def calculate_perimeter(self):
        return self.a + self.b + self.c

class Circle(Shape):
    def __init__(self, colour, radius):
        super(Circle, self).__init__(colour)
        self.radius = radius
        self.shape_type = 'Circle'
        
    def calculate_area(self):
        return math.pi * self.radius ** 2 
        
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, colour, side):
        super(Square, self).__init__(colour)
        self.side = side
        self.shape_type = 'Square'
    
    def calculate_area(self):
        return self.side ** 2
        
    def calculate_perimeter(self):
        return 4 * self.side
        
    
c = Circle('red', 3)
c.calculate_area()
c.to_string()
c.calculate_perimeter()

s = Square('blue', 5)
s.calculate_area()
s.to_string()
s.calculate_perimeter()

t = Triangle('green', 4, 4, 3)
t.calculate_area(), t.shape_type

t.to_string()
t.calculate_perimeter()

c.print_area_and_perimeter()
s.print_area_and_perimeter()
t.print_area_and_perimeter()