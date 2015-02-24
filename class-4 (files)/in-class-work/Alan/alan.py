
class Unicorn(object):
    def __init__(self, name):
        self.name = name
        self.superpower = 'flying'
        self.powerLevel = 1
        
    def __str__(self):
        return "My name is {} and I am a unicorn.".format(self.name)
        
    def __gt__(self, other):
        return self.powerLevel > other.powerLevel
        
    @property
    def color(self):
        color = 'purple'
        
    @staticmethod
    def talk(string):
        print "unicorns sometimes say {}".format(string)
    
    @classmethod
    def unicorn_fleet(cls, data):
        unicorns = []
        for name in data:
            new_unicorn = cls(name=name)
            unicorns.append(new_unicorn)
        return unicorns
        
    
    
    