##Json(JavaScript Object Notation) module allows you to dump simple Python data structures into a file and load the data from that file the next time program runs.
# Using json.dump() and json.load()
import json            # Import json module

numbers = [23, 78, 900, 77]

filename = 'numbers.json'   # use extension .json to indicate data in the file is stored in JSON format

with open(filename, 'w') as obj:
    json.dump(numbers, obj)

# Now we write a program that uses json.load() to read the list above back into memory.
import json

filename = 'numbers.json'
with open(filename) as obj:
    numbers = json.load(obj)

print(numbers)

## Saving and reading user-generated data
# Load the username if it has been stored previously, otherwise propmt for it and store it.
import json

filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)

except FileNotFoundError:
    username = input("Enter your name ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("I'll remember you when you return, " + username)

else:
    print("WELCOME BACK " + username + "!")


