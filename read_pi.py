# Working with a file's contents after you have read a file into a list or memory.
filename = 'pi.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()  # Adds each line of digits to pi_string, and removes newline character.

print(pi_string)
print(len(pi_string))
