# 2create the same "Person" class, but set the attributes in the initialization special method.

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


martin = Parson(name="Martin", 30)

print martin.name
print martin.age

