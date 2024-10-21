# The input() function pauses your program and waits for the user to enter some text.
# User's input is stored in a variable to make it convenient for you to work with.
text = input('Tell us your first name: ')
print('Welcome ' + text + '!')

# Example 2, build a multi-line string
text1 = 'Good to have you in our online platform.'
text1 += '\nWhat is your last name? '  # The operator += adds another string at the end first string

name = input(text1)
print('\nHello ' + name + '!')

# The int() function tells python to treat the input as a numerical value
age = input('What is your age? ')
age = int(age)

if age >= 18:
    print('\nYou are qualified.')
else:
    print('\nTry next time, thank you for interest.')

# The modulo operator divides one number by another and returns the remainder, e.g 5 % 3 is 2
print('\nNow do some computing!')
number = input('Enter a number, is it odd or even? ')
number = int(number)

if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.')



