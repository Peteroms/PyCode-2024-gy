# The file write() function doesnt add any newlines, to do so type \n at the end of each line.
# The open() function must have a second argument, w, to tell python we are openning file im write mode.
filename = 'game.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love game of thrones.\n")
    file_object.write("I like sudoku game.\n")

# APPENDING TO A FILE: Add content to file in the append mode rather than writing over the existing file.
with open(filename, 'a') as file_object:
    file_object.write("I wanted to act in film industry. \n")
    file_object.write("Like Marvels.\n")



