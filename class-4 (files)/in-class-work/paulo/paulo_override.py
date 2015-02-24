class Car(object):

    def __init__(self):
        self.type = type

    def movement(type):
        print("{} on land only".format(self.type))
        
class Boat(type):
    def __init__(self):
        self.type = type
    
    def movement(type):
        print("{} on water only".format(self.type))
        
class Hovercraft(Boat, Car):
    pass

i = Hovercraft('speedboat')
i.movement()
    