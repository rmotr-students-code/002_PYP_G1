# create a "Person" empty class, initialize a person object, and set some attributes.

# create the same "Person" class, but set the attributes in the initialization special method.

# # Augment the "Person" class with the following instance methods (add any new attributes to the Person class if needed): 
# get_age:  # calculates the age based in the birth date
# get_full_name:  # concatenation of first_name and last_name.
# is_female:  # returns True if the gender is female.
# add_friend:  # receives another Person object as parameter and adds it to the list of friends.


class Person(object):
    def __init__(self, age, first_name, last_name, hobby, birthdate):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.hobby = hobby
        self.birthdate = birthdate
        
    #functions inside the class , is_female, add_friend)
    def get_age(self): #birthdate!...
        return 2015 - int(self.birthdate[-4:]) #

    def get_full_name(self):
        return str(self.first_name) + ' ' +str(self.last_name)

p = Person(28, 'Paulo', 'Gonzalez', 'tennis', '11/22/1987')

print(p) # cool, knows it is an object! <__main__.Person object at 0x7f2a701c5450>  
print(p.get_age())
print(p.get_full_name())
