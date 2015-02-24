# create a "Person" empty class, initialize a person object, and set some attributes.

# create the same "Person" class, but set the attributes in the initialization special method.


class Person(object):
    def __init__(self, weight):
        self.weight = weight
        
w = Person(weight = 150)

print(w.weight)
