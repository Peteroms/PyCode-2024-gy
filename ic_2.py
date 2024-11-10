# Importing an entire module, and access the classes you need using dot notation.
import ic

my_car = ic.Car('mercedes', 'model 56', 2007)
print(my_car.car_describe())

my_electric = ic.ElectricCar('Tesla', 'TY7', 2026)
print(my_electric.car_describe())


