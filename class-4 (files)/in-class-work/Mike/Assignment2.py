class CombatAthlete(object):
    def __init__(self, full_name, weight, rating):
        self.full_name = full_name
        self.weight = weight
        self.rating = rating
        
    def action(self):
        print "{} has thrown a punch.".format(self.full_name)
    
class BasketballPlayer(object):
    def __init__(self, full_name, weight, rating):
        self.full_name = full_name
        self.weight = weight
        self.rating = rating
        
    def action(self):
        print "{} has shot the ball.".format(self.full_name)
        
class FootballPlayer(BasketballPlayer, CombatAthlete):
    pass

fb1 = FootballPlayer('Mike A', 150, 10)

fb1.action()


