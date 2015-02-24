
class Person(object):
    def __init__(self, fname, lname, birthday, gender):
        self.fname = fname
        self.lname = lname
        self.birthday = birthday
        self.gender = gender
        self.friends = []
        
    def get_age(self):
        if len(self.birthday) > 4:
            birthyear = int(self.birthday[-4:])
        else:
            birthyear = self.birthday 
        currentyear = 2015
        age = currentyear - birthyear
        return age
        
    def get_full_name(self):
        return self.fname + " " + self.lname
    
    def is_female(self):
        female = True
        if "male" in self.gender.lower():
            female = False
    
    def add_friend(self, new_friend):
        self.friends.append(new_friend)
        
        
        
        
        