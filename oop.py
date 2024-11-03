# Create classes that represent real world situations. Create objects based on the class (instantiation).
# Store the classes in modules
# Example 1:
class Hotel():
    '''A simple attempt to model a hotel'''

    def __init__(self, name, cuisine_type): # Self parameter is a must in init method definition.
        self.name = name # Takes the value stored in parameter name, stores it in the variable name (attribute).
        self.cuisine_type = cuisine_type

    def describe_hotel(self):
        print('\nMy hotel name is ' + self.name + '. It offers ' + self.cuisine_type + ' foods, welcome!')

    def open_hotel(self):
        print('The hotel ' + self.name + ' is OPEN!')


class Hotel():  # Instances
    hotel = Hotel('Leech', 'Chinese')
    hotel_2 = Hotel('savanna', 'African')

    print('I loved ' + hotel.name.title() + '.')
    print('We ate amazing ' + hotel.cuisine_type + ' meals.' )
    hotel.describe_hotel()
    hotel.open_hotel()

    print('\nI aslo own hotel ' + hotel_2.name + '.')
    print('It has ' + hotel_2.cuisine_type + ' meals.')
    hotel_2.describe_hotel()
    hotel_2.open_hotel()



# Example 2:
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('\nThis is a summary of the user: ' + self.first_name + ' ' + self.last_name)

    def greet_user(self):
        print('Hello ' + self.first_name + ' ' + self.last_name)

class User():
    user_1 = User('Kelvin', 'Ouma')
    user_2 = User('Nick', 'jane')

    user_1.describe_user()
    user_1.greet_user()

    user_2.describe_user()
    user_2.greet_user()


