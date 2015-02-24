
class Human(object):
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print "Hello, my name is {}".format(self.name)

class Fly(object):
    def __init__(self):
        self.legs = 4
    
    def talk(self):
        print "bzzzz"
        

class Human_fly_monster(Fly, Human):
    def __init__(self, name):
        self.name = name
        
seth_brundle = Human_fly_monster('Seth')

seth_brundle.talk()

