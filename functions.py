# Functions are named blocks of code designed to do one specific job
# You can store functions in separate files called modules to help organize your main program files
def greet():  # Function definition
    '''Display a simple greeting'''  # The text is a comment called docstring, describes what fucntion does
    print('HI!')

greet() # call the function

# Passing information to a function
def hello(user): # The variable user in hello(user) is called a parameter.
    '''display a greeting'''
    print('Hello, ' + user.title() + ', welcome!')

hello('Peter')  # The fuction allows any value provided for user, this value is called an argument.

# Passing arguments to a function using postional arguments and keyword arguments
# Positional argument: Note that Order matters in positional arguments.
def program(user, software):
    '''dispaly information on a user's program'''
    print('\nI, ' + user.title() + ' love ' + software.title())
    print('That is good')

program('ronald', 'python')
program('rose', 'C')

# Keyword arguments
program(user='john', software='matlab')
program(user='clarice', software='javascript')

# Default values
def pet(name, pet_type='cat'):
    print('my pet name is ' + name + ', it is a ' + pet_type)

pet(name='sussy')

# Return values is used when a function doesnt have to display its output directly.
def named_format(first, last):
    full_name = first + ' ' + last
    return full_name.title()

student = named_format('Jude', 'Alexas')
print(student)

# Making an Argument optional
def cloth(condition, shop, colour=''):
    if colour:
        cloth_status = condition + '  ' + colour + ' ' +  shop
    else:
        cloth_status = condition + ' ' +  shop
    return cloth_status.title()

choice = cloth('bad', 'A', 'Red')
print(choice)

choice = cloth('good', 'B')
print(choice)

# Returning a dictionary
def personas(first_name, last_name, age='', location=''):
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

identity = personas('Erick', 'James', age=18)
print(identity)

# Using a function with a while loop
def survey(second_name, sir_name):
    full_name = second_name + ' ' + sir_name
    return full_name.title()

while True:
    print('\nEnter your names:')
    sec_name = input('Second name:')
    si_name = input('Enter Sir name:')
    if sec_name == 'Q':
        break
    elif si_name == 'Q':
        break

results = survey(sec_name, si_name)
print('\nHello ' + results)

# Passing a list to a function
def greetings(names):
    for name in names:
        message = 'Hello, ' + name.title()
        print(message)

users = ['lavender', 'joshua', 'kalx', 'irene']
greetings(users)

# Modifying a list in a function
def dresses(trials, finished):
    while trials:
        new_trial = trials.pop()
        print('\nMaking in process: ' + new_trial)
        finished.append(new_trial)

def show_dresses(finished):
    print('\nThe following dresses are complete:')
    for finish in finished:
        print(finish)

trials = ['blue dress', 'white dress', 'pink dress']
finished = []

dresses(trials, finished) # To use a copy of the original list to prevent emptying the oiginal, the function can be written as: dresses(trials[:], finished)
show_dresses(finished)

# Passing an arbitrary number of arguments. The * in parameter name tells python to make an empty tuple called fruits
def food(number, *fruits):
    print('\nMake a list of fruitts:')
    for fruit in fruits:
        print(str(number) + ' Fresh ' + fruit)

food(14, 'banana', 'orange', 'pinapple', 'lemon')

# Using arbitrary keyword arguments
def profiling(name, place, **other_info):
    profile = {}
    profile['first_name'] = name
    profile['living_place'] = place
    for key, value in other_info.items():
        profile[key] = value
    return profile

user_profile = profiling('petros', 'germany', language='english', field='software')
print(user_profile)





