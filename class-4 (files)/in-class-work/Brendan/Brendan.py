class Square(object):
    
    def __init__(self, colour, name, side_length):
        self.colour = colour
        self.name = name
        self.side_length = side_length
    
    def __str__(self):
        return 'The {colour} {name} exists!'.format(colour=self.colour, name=self.name)
    
    def __gt__(self, other):
        return self.area > self.other
    
    @staticmethod
    def calc_area(side_length):
        return side_length ** 2
        
    @property
    def area(self):
        return Square.calc_area(self.side_length)
        
    @property
    def perimeter(self):
        return 4 * self.side_length
    
    @classmethod
    def create_multiple(cls, entry):
        shape_list = []
        
        for colour, name, side_length in entry:
            new_object = cls(colour=colour, name=name, side_length=side_length)
            
            shape_list.append(new_object)
        
        return shape_list

objects = Square.create_multiple([('red', 'Square1', 4), ('yellow','Square2', 3), ('green', 'Square3', 9)])

for object_ in objects:
    print object_

print objects[0] > objects[1]

sq = Square('orange', 'square4', 12)

print sq.area
    