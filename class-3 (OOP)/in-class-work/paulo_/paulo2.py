# # create a "Shape" abstract class, and implement 3 classes that inherit from it: Triangle, Circle, Square. 
# Each class has to be able to perform the following method:
# to_string:  # returns a string explaining the shape type and color
# calculate_area:  # returns the shape area depending on the shape type
# calculate_perimeter:  # returns the shape perimiter depending on the shape type

class Shape(object):
    def __init__(self, shape_type, shape_color, shape_base, shape_height):
        self.shape_type = shape_type
        self.shape_color = shape_color
        self.shape_base = shape_base
        self.shape_height = shape_height
    
    def to_string(self):
        return 'this is a ' + str(self.shape_type) + ' and it is ' + str(self.shape_color)


class Triangle(Shape):
    self.shape_type = 'triangle'
    def calculate_area_triangle(self):
        a = (self.shape_base * self.shape_height)/2
        return 'The area of the " str(self.) is '+ str(a)


class Circle(Shape):
    def calculate_area_Circle(self):
        a = ()
        return 


class Square(Shape):
    pass

#tests
s = Shape('triangle', 'red', 4, 4)
print(s.to_string(), 'Shape class')
#t = Triangle('triangle', 'red', 4, 4)
t = Triangle('red', 4, 4)
print(t.to_string(), 'Triangle class') 
print(t.calculate_area_triangle(), 'Triangle class')