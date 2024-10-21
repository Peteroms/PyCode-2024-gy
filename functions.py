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




