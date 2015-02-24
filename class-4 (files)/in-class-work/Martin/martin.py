#https://gist.github.com/martinzugnoni/ecb1196d334699cf174c

data = [
    ("Toyota", "Camry","2015","grey"),
    ("Ford", "Mustang","2011","green")
    ]


class Car(object):
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    def __str__(self):
        return "You've created a {}, {} {}".format(self.year, self.make, self.model)
    
    def paint_job(self, new_color):
        self.color = new_color
    
    @property
    def km_per_litre(self):
        if self.make == "Toyota":
            return 15.00
        else:
            return 20.00
    
    @staticmethod
    def gastank_refills(distance,mileage):
        return distance/mileage
        
    @classmethod
    def create_cars(cls, data):
        cars = []
        for make, model, year, color in data:
            new_car = cls(make = make, model = model, year = year, color = color)
            cars.append(new_car)
        return cars
 
cars = Car.create_cars(data)

for i in cars:
    print i