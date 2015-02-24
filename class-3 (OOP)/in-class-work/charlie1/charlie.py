# create a "Person" empty class, initialize a person object, and set some attributes.

class Person(object):
    
    def __init__(self, birth_year, first_name, last_name, gender):
        self.birth_year = birth_year
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.friends = []
    
    def __unicode__(self):
        return self.get_full_name()
        
    def __str__(self):
        return self.get_full_name()
    
    def get_age(self):
        return 2015 - int(self.birth_year)
        
    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name]).title()
    
    def is_female(self):
        return self.gender.lower() == 'female'
        
    def add_friend(self, new_friend):
        self.friends.append(new_friend)
        return "You have added {} as a friend".format(new_friend.get_full_name())    
        
charlie = Person(1992, 'charles', 'lee', 'male')

assert charlie.get_age() == 23
assert charlie.get_full_name() == 'Charles Lee'
assert charlie.is_female() == False

new_friend = Person(1992, 'coffee', 'cup', 'female')
assert charlie.add_friend(new_friend) == "You have added Coffee Cup as a friend"
assert [str(o) for o in charlie.friends] == ['Coffee Cup']


your_age = int(input("What year were you born in?"))
your_firstname = input("What is your FIRST name?")
your_lastname = input("What is your LAST name?")
your_gender = input("Are you a male or a female?")

you = Person(your_age, your_firstname, your_lastname, your_gender)

charlie.add_friend(you)
assert [str(o) for o in charlie.friends] == ['Coffee Cup', '{}'.format(you.get_full_name())]

# good job
# thanks 