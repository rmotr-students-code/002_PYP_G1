"""Example demonstrating classes and properties"""

class Animal(object):
    
    def __init__(self, type, color, size, weight):
        self.type = type
        self.color = color
        self.size = size
        self.weight = weight
        
    def __str__(self):
        #return '{} is an animal it weighs {} and it is {}'.format(self.type, self.weight, self.size) # ok
        return '{} is an animal it weighs {} and it is {}'.format(self.type, self.calculate_weight_kilo(), self.size)

    @property
    def animal_size(self):
        return self.size

    @staticmethod
    def calculate_weight_kilo(weight): # not good
        weight_kilo = float(weight_lbs/2.2)
        return weight_kilo
    


print(Animal('Sheep', 'white', 'huge', 160))
#print(Animal())