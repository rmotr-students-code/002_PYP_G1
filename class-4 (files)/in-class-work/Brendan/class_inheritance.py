import math

class Square(object):
    
    def __init__(self, distance):
        self.distance = distance
    
    def area(self):
        return self.distance ** 2

class Circle(object):
    
    def __init__(self, distance):
        self.distance = distance
    
    def area(self):
        return math.pi * self.distance ** 2
        
class Shape(Circle, Square):
    
    def __init__(self, distance):
        self.distance = distance

shape1 = Shape(4)

print shape1.area()