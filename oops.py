class Car():
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print('This ', self.model, ' is driving.')
    def stop(self):
        print('This ', self.model, ' is stopped.')

car1 = Car('tata', 'harrier', 2021, 'white')
car2 = Car('Bugatti','veyron', 2015, 'red')

print(car1.make, car1.model, car1.year, car1.color)

print('\n')

print(car2.make)
print(car2.model)
print(car2.color)

car1.drive()
car2.stop()