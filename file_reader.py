# This program file reads an entire text file, the open() function takes one argument, the name of the file you want to open. e.g assuming both files are in same directory;
with open('dictionaries.py') as file_object:
    contents = file_object.read()
    print(contents)


# FILE PATHS:

# A relative path tells Python to look for a given location relative to the directory on which the program file is stored. e.g assuming moduless is the directory with the text file;
#       with open('modules/filename.txt') as file_object

# Absolute paths are usually longer than relative paths, its helpful to store them in a variable and pass the variable to open().
#       file_path = ' /home/other_files/moduless/filename.txt'
#       with open(file_path) as file_object:

# READING LINE BY LINE
# You can use a for loop on the file object to examine each line from a file one at a time
filename = 'oop.py'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# Using rstrip() on each line in the print statement eliminates the extra blank lines. i.e print(line.rstrip()).

## Making a list of lines from a file, use the readlines() method that takes each line from a list and stores in a list.
filename = 'oop.py'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())









