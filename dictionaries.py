## A dictionary in Python is a collection of key-value pairs.
# You can use a key to access a value associated with that key
# Dictionaries are wrapped in braces, {}
# Accessing values in a Dictionary, give the name of the dictionary and then place the key inside a set of square brackets
games = {'football':'manchester', 'points':'FIVE', 'league':'England'}
print(games['football'] + ' play in ' + games['league'] + ', the are number ' + games['points'])

# Adding  key-values to the dictionary
games['players'] = 5
games['coach'] = 'alex'

print(games)

# Starting with an empty dictionary
player = {}
player['colour'] = 'Red'
player['points'] = 40
player['shirt'] = 1

print(player)

# Modifying values in a dictionary
car = {'x_position':0, 'speed':'medium'}
if car['speed'] == 'slow':
    x_increment = 1
elif car['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

car['x_position'] = car['x_position'] + x_increment
print('The New car position is ' + str(car['x_position']))

# Removing a key-value pair, use del statement e.g del car['x_position']
# Breaking a larger dictionary into several lines e.g storing the results of a poll
favorite_program = {
        'lucy': 'python',
        'peter':'java',
        'nelson':'c',
        'john':'bash',
        }
print('Lucy loves ' +
        favorite_program['lucy'].title() +
        ', yeah!')

## LOOPING THROUGH A DICTIONARY
# You can loop through key-value pairs, through its keys or its values.
# Looping through all key-value pairs
users = {
        'username':'fermi',
        'first':'rico',
        'last':'femi'
        }

for key, value in users.items():  # items() returns a list of key-value pairs.
    print('\nkey: ' + key)
    print('value: ' + value)

# Looping through all keys using keys()
for k in users.keys():
    print(k.title())

# You can access the value associated with any key you want
attribute = ['first', 'username']
for k in users.keys():
    print(k.upper())
    if k in attribute:
        print('Enter ' + k.upper() + ' My name is ' + users[k].title())

# Looping throuh dictionary's keys in order, use the sorted()
for k in sorted(users.keys()):
    print(k.upper())

# Looping through all values using values() method
for k in users.values():
    print(k.lower())

# To pull out a large a number of values without repetition, use set() function
for k in set(users.values()):
    print(k.upper())
