#override classe inheritance

class Creature():
    def speak(self):
        print('Creature speak')
        
        
class Insect():
    def speak(self):
        print('Insect speak')
        
        
class Ant(Insect, Creature):
    pass


bob = Ant()
bob.speak()
