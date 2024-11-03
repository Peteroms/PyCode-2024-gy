# Working with classes and instances
# Have  methods to  summarize attributes information
class Car():
    '''A simple attempt to represent a car'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 10 # this is to set a default value for an  attribute

    def car_describe(self):
        the_name = self.make + ' ' + self.model + ' ' + str(self.year)
        return the_name.title()

    def read_mileage(self):
        print('This car has a mileage of ' + str(self.mileage) + ' on it')

my_car = Car('bmw', 's2', 2024)
print(my_car.car_describe())
my_car.read_mileage()


# Modifying attribute values directly through an instnace e.g
my_car.mileage = 200
my_car.read_mileage()

# Modifying through a method e.g








