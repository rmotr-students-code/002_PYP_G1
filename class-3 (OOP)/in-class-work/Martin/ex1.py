#1 create a "Person" empty class, initialize a person object, and set some attributes.
class Person(object):
    pass

martin = Parson()
martin.name = "Martin"
martin.age = 29

# 2create the same "Person" class, but set the attributes in the initialization special method.

# 3Augment the "Person" class with the following instance methods (add any new attributes to the Person class if needed): 
get_age:  # calculates the age based in the birth date
get_full_name:  # concatenation of first_name and last_name.
is_female:  # returns True if the gender is female.
add_friend:  # receives another Person object as parameter and adds it to the list of friends.