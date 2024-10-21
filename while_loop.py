# In contrast to the for loop which executes a block of code once for each item in a collection, the while loop runs as long as, or while, a certain condition is true
number = 1
while number <= 6:
    print(number)
    number += 1

# Example, letting user choose when to Quit
text = '\nTell the movies you like. '
text += "\nEnter 'quit' to end: "

name = ''
while name != 'quit':
    name = input(text)
    print(name)



