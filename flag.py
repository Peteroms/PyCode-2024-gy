# Use a flag, for a program that should run only as many conditions are true
prompt = '\nTell me something '
prompt += "\nEnter 'quit' to end:  "

flag = True
while flag:
    message = input(prompt)
    if message == 'quit':
         flag = False
    elif message == 'end':
         flag = False
    else:
         print(message)

# Use break to exit a while loop immediately without running any remaining code in the loop
text = '\nWhat is your favorite town?'
text += "\nEnter 'quit' to finish:  "

while True:
    town = input(text)

    if town == 'quit':
        break
    else:
        print(town)

# Using while loops with lists and dictionaries
# Moving items from one list to another
new_users = ['rose', 'jane', 'carol', 'james']
comfirmed_users = []

while new_users:
    current_users = new_users.pop()

    print('\nverifying user: ' + current_users.title())

    comfirmed_users.append(current_users)

print('\nThe following users have been comfirmed: ')
for user in comfirmed_users:
    print(user.title())

# Removing all instances of specific values from a list
my_pets = ['cat', 'hare', 'dog', 'hare', 'panda', 'hare']
print(my_pets)

while 'hare' in my_pets:
    my_pets.remove('hare')

print(my_pets)

# Filling a dictionary with user input e,g a polling exercise
responses = {}

poll_active = True

while poll_active:
    name = input('\nWhat is your first name? ')
    Quiz = input('Which city will you like to travel? ')

    responses[name] = Quiz

    redo = input('Would you let another person to take the poll? (Yes/ No: ')
    if redo == 'no':
        poll_active = False

print('\n..The poll results are as follows..')
for name, Quiz in responses.items():
    print(name + ' would like too visit ' + Quiz + '.')










