class Shape(object):
	def __init__(self, shape, color):
		self.shape = shape
		self.color = color

	def to_string(self):
		return "I'm a {0} shape, and I'm colored {1}".format(self.shape, self.color)
		
		
class Triangle(Shape):
    def __init__(self, side_length):
        self.sides=3             
        self.side_length = side_length
        self.shape = "triangle"
        super(Triangle, self).__init__(shape, color)

    def calculate_area(self):
        return (side_length * side_length) / 2
        
        
    def calculate_perimeter(self):
       return side_length * 3
       
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.shape = "circle"
        
        
    def calculate_area(self):
        area = 3.14 * (self.radius) **2
        return area
        
    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
    
class Square(Shape):
    def __init__(self, sides, side_length):
        self.shape = "square"
        self.sides = 4
        self.side_length = side_length
    
    def calculate_area(self):
        return side_length * side_length
        
    def calculate_perimeter(self):
        return side_length * sides
    
