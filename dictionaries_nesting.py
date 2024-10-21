## A list of dictionaries
# Example 1
car_1 = {'colour':'red', 'speed':'low', 'position': 1}
car_2 = {'colour':'green', 'speed':'medium', 'position': 2}
car_3 = {'colour':'blue', 'speed':'fast', 'position': 3}

cars = [car_1, car_2, car_3]
for car in cars:
    print(car)

# Example 2: Use range() to create a fleet of cars
cars = []
for car in range(10): # range() returns a set of numbers, tells python how many times the loop is repeated
    new_car = {'colour':'purple', 'speed':'medium', 'position': 7}
    cars.append(new_car)

for c in cars[:5]:
    print(c)

# A list in dictionary; more than one value associated with a single key
pizza = {
        'crust':'thick',
        'toppings':['mushrooms', 'extra cheese'],
        }

print('This is your order, a ' + pizza['crust'] + '-crust pizza with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)

# A dictionary in a dictionary, e.g if you have several users in a website, each with unique name
usernames = {
        'userA':{
            'first': 'albert',
            'last': 'kenny',
            'region': 'newyork'
            },
        'userB':{
            'first': 'jane',
            'last': 'meghan',
            'region': 'nairobi'
            }
        }

for names, user_info in usernames.items():
    print('\nUsername: ' + names)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['region']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())


