''' A set of classes representing electric cars'''
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def car_describe(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' mileage.')

class Battery():
    def __init__(self, battery_size=30):
        self.battery_size = battery_size

    def battery_describe(self):
        print('This car has a ' + str(self.battery_size) + ' kwh battery.')

    def get_span(self):
        if self.battery_size == 30:
            span = 120
        elif self.battery_size == 75:
            span = 180

        message = 'This car can go for ' + str(span)
        message += ' Miles depending on battery'
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


















