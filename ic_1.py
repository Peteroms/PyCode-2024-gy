# You can import a class or multiple classes from a moudle. In case of multiple classes, use a comma to separate the classes
from ic import Car, ElectricCar

my_car = Car('Toyota', 'T17', 2005)
print(my_car.car_describe())

my_electriccar = ElectricCar('BMW', 'B10', 2025)
print(my_electriccar.car_describe())
