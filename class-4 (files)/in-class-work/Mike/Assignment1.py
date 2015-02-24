class Athlete(object):
    def __init__(self, full_name, weight, sport, rating):
        self.weight = weight
        self.sport = sport
        self.rating = rating
        
    def __str__(self):
        return "{}, a {} pound {} with a player rating of {}.".format(self.full_name, self.weight, self.sport, self.rating)
        
    def __gt__(self, other):
        return self.rating > other.age
        
    @property
    def adj_rating(self):
        return Athlete.adjusted_rating(self.rating)
        
    
    @staticmethod
    def adjusted_rating(rating):
        return rating / 2
    
    @classmethod
    def reduce_rating(cls, reduction):
        for 
        
        
        
athlete_list = [a1, a2, a3]
Athlete.reduce_rating(a1, a2, a3)