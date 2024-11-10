# iNHERITANCE: When a child class inherits attributes and methods from a parent class
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

class ElectricCar(Car):  # Name of parent class must be included in the parenthesis
    '''Represnt aspects of an electric car'''
    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class.'''
        super().__init__(make, model, year)  # The super() function helps Python make connections between the parent and child class.
        self.battery_size = 100 # Defining new attributes and methods for the child class

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + ' kwh battery')

my_car = ElectricCar('ford', 'model M', 2024)
print(my_car.car_describe())
my_car.describe_battery()

# Overriding Methods from parent class, define a method in the child class with the same name as the method in the parent class you want to override.

# Instances as attributes
#    class Car():
#        --snip--

#    class Battery():
#      def __init__(self, battery_size=170):
#         self.battery_size = battery_size

#    class ElectricCar(Car):
#        __snip__
#         self.battery = Battery()

# my_car = ElectricCar('tesla, 'gm', 2018)
# my_car.battery.describe_battery()


