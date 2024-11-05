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
class Cement():
    def __init__(self, colour, new_price):
        self.colour = colour
        self.new_price = new_price

    def read_prices(self):
        prices = self.colour + ' ' + str(self.new_price)
        return prices

    def update_price(self, price):
        '''set the new_price to the given value'''
        self.new_price = price

cement_values = Cement('Blue', 1000)
cement_values.update_price(2000)
print(cement_values.read_prices())

# Increamenting an attribute's value through a method
class Vehicle():
    def __init__(self, brand, origin):
        self.brand = brand
        self.origin = origin
        self.dates = 2002

    def update_vehicle(self, times):
        self.dates += times

    def description(self):
        desc = self.brand + ' ' + self.origin + ' ' + str(self.dates)
        return desc

my_vehicle = Vehicle('Limo', 'Whales')
print(my_vehicle.description())

my_vehicle.update_vehicle(30)
print(my_vehicle.description())











