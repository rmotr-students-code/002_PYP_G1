class Person(object):
    def __init__(self, weight, birthday, first_name, last_name, gender, friends):
        self.weight = weight
        self.birthday = birthday
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.friends = []
        
    def get_age(self):
        return 2015 - self.birthday
        
    def get_full_name(self):
        return self.first_name + " " + self.last_name
        
    def is_female(self):
        return True if self.gender == 'female' else False
    
    def add_friend(self, friend):
        self.friends.append(self.friend)
        return self.friends
        
        
mike = Person(weight = 150, birthday = 1985, first_name = 'Michael', last_name = 'Azar',gender = 'male')
john = Person(weight = 140, birthday = 1988, first_name = 'John', last_name = 'Smith',gender = 'male')

mike.add_friend(John)

