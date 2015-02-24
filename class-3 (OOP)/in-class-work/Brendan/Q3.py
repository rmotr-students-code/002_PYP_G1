"""# Augment the "Person" class with the following instance methods (add any new attributes to the Person class if needed): 
get_age:  # calculates the age based in the birth date
get_full_name:  # concatenation of first_name and last_name.
is_female:  # returns True if the gender is female.
add_friend:  # receives another Person object as parameter and adds it to the list of friends.
"""

class Person(object):
    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = int(birth_date)
        self.gender = gender
        self.friends_list = []
        self.present_year = 2015
    
    def get_age(self):
        return self.present_year - self.birth_date
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
        # print 'This persons name is {} {}'.format(self.first_name, self.last_name)
    
    def is_female(self):
        if self.gender.lower() == 'female':
            return True
        else:
            return False
    
    def add_friend(self, friend):
        self.friends_list.append(friend.get_full_name())

p1 = Person('Brendan', 'Emery', 1994, 'Male')
print p1.get_full_name()
print p1.is_female()
print p1.get_age()

p2 = Person('John', 'Blog', 1980, 'Female')
print p2.get_full_name()
print p2.is_female()
p2.add_friend(p1)
print p2.get_age()

p3 = Person('Jess', 'tes', '1990', 'FEMALE')
print p3.get_full_name()
print p3.is_female()
print p3.get_age()
p2.add_friend(p3)
print p2.friends_list