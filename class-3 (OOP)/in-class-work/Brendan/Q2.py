# create the same "Person" class, but set the attributes in the initialization special method.

class Person(object):
    def __init__(self, name, height):
        self.name = name
        self.height = height

p1 = Person(name="Brendan", height="180cm")
p2 = Person(name="John", height="170cm")

print p1.name
print p1.height

print p2.name
print p2.height