# Augment the "Person" class with the following instance methods (add any new attributes to the Person class if needed): 
#get_age:   calculates the age based in the birth date
#get_full_name:   concatenation of first_name and last_name.
#is_female:   returns True if the gender is female.
#add_friend:   receives another Person object as parameter and adds it to the list of friends.

class Person(object):
    def __init__(self, first_name, last_name, birth_year, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.sex = sex
        self.friends = []

    def get_age(self, current_year):
        age = int(current_year) - int(self.birth_year)
        return age
        
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
        
    def is_female(self):
        if self.sex.lower() == 'female':
            return True
        else:
            return False

    def add_friend(self, new_friend):
        self.friends.append(new_friend)
        
        
martin = Person("Martin", "Lats", 1985, "Male")
james = Person("James", "Junior", 1990, "male")

martin.add_friend(james.get_full_name())
print martin.friends

