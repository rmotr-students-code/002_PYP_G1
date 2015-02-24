# Keep away from paulo. 

from math import pi

class Shape(object):
    
    def __init__(self):
        raise NotImplementedError("Hey, this is an abstract class")
    
    def to_string(self):
        try:
            return "This is a {} that is {}".format(self.shape, self.color)
        except:
            # raises error if Shape object is made. 
            raise NotImplementedError("Hey, this is an abstract class")
    
    def calculate_area(self):
        raise NotImplementedError()
        
    def calculate_perimeter(self):
        raise NotImplementedError()
    
    def all_details(self):
        try: 
            return "Shape: {}, Color: {}, Area: {}, Perimeter: {}".format(self.shape, self.color, self.calculate_area(), self.calculate_perimeter())
        except: 
            raise NotImplementedError("Hey, this is an abstract class")
            
class Square(Shape):
    
    def __init__(self, color, height, width):
        self.color = color
        self.height = height
        self.width = width
        self.shape = 'square' 
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2*self.width + 2*self.height

example_square = Square('blue', 5, 5)
assert example_square.to_string() == "This is a square that is blue"
assert example_square.calculate_area() == 25
assert example_square.calculate_perimeter() == 20
        
class Triange(Shape):
    
    def __init__(self, color, side1, side2, side3, height, base):
        self.shape = 'triangle'
        self.color = color
        self.side1,self.side2,self.side3 = side1,side2,side3
        self.base = base
        self.height = height
        
    def calculate_area(self):
        return float(self.base * self.height / 2)
        
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
        
example_triangle = Triange('red', 3, 4, 5, 4, 3)
assert example_triangle.to_string() == "This is a triangle that is red"
assert example_triangle.calculate_area() == 6
assert example_triangle.calculate_perimeter() == 12

class Circle(Shape):
    
    def __init__(self, color, radius):
        self.shape = 'circle'
        self.radius = radius
        self.color = color
        
    def calculate_area(self):
        return pi*(self.radius**2)
        
    def calculate_perimeter(self):
        return 2*pi*self.radius
        
example_circle = Circle('yellow', 4)
assert example_circle.to_string() == "This is a circle that is yellow"
assert example_circle.calculate_area() == pi*(4**2)
assert example_circle.calculate_perimeter() == 2*pi*4
assert example_circle.all_details() == "Shape: circle, Color: yellow, Area: {}, Perimeter: {}".format(pi*(4**2), 2*pi*4)



# Notes:

# R @instance_variable == P self.instance_variable
