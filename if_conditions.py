# Simple example: The loop first checks if the current value in car is 'bmw', if it is the value is printed in uppercase.If value is anything other than 'bmw' it is printed in title case
cars = ['toyota', 'bmw', 'mercedis']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Check multiple conditions using keyword and to evaluate if all statements are true or false. (You can use keyword or to test if either statements is true)
age_1 = 20
age_2 = 30
if age_1 <= 22 and age_2 >= 25:
    print('True')
else:
    print('False')

# Check whether a value is in a list using keyword in. (To check if value is not on list, you can use keywords not in)
fruits = ['banana', 'oranges', 'tomatoes', 'apple']
fruit = 'apple'
if fruit in fruits:
    print('Good!' + ' ' + 'I love' + ' ' + fruit.upper())

# The if-elif-else conditions:
age = 18
if age < 19:
    price = 50
elif age < 10:
    price = 20
else:
    price = 100
print('Your cost is $' + str(price))
# If you are having a specific final condition, consider using a final elif block instead of an else block wich is a catchall block
# If you want to check all conditions of interest, use if statement without elif or else block
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'extra cheese' in requested_toppings:
    print("Adding pepperoni.")

# For loop with if statements
fruit_colour = ['orange', 'green', 'purple', 'black']
for colour in fruit_colour:
    if colour == 'black':
        print('Dispose this fruit')
    else:
        print('These colours: ' + colour + 'show a good fruit.')

# Checking that a list is empty
snacks = []
if snacks:
    for snack in snacks:
        print('I love the snack!')
else:
    print('Request a snack')

# USING  MULTIPLE LISTS
available_religions = ['Christianity', 'Islam', 'Hinduism', 'Paganism']
popular_religions = ['Christianity', 'Judaism', 'Islam']
for religion in popular_religions:
    if religion in available_religions:
        print('Yes that is  ' + religion)
    else:
        print('I will research on ' + religion)

