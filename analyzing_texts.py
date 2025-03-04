# We can use split() method to build a list of words from a text, and store in a list.
filename = 'loop.py'

try:
    with open(filename) as f_obj:
        content = f_obj.read()

except FileNotFoundError:
    msg = 'No Such File Exists!'
    print(msg)

else:
    words = content.split()
    num_words = len(words)
    print('The file ' + filename + ' has approximately ' + str(num_words) + ' words')

## Working with multiple files
# Good to move the bulk of this program to a function, itll be eaisr to analyze multiple files
def count_words(filename):
    '''Counting number of words in multiple files'''
    try:
        with open(filename) as obj:
            cont = obj.read()
    except FileNotFoundError:
        print("File missing!")

    else:
        words = cont.split()
        num_words = len(words)
        message = "The file " + filename + " has around " + str(num_words) + " words"
        print(message)

filenames = ['loop.py', 'ic.py', 'flag.py', 'rom.txt', 'pi.txt']
for filename in filenames:
    count_words(filename)

## Failing Silently: When you dont want to report every exception you catch.
# Write a try block as usual, but you explicity tell Python to do nothing int the except block using a 'pass' statement
#     try:
#       --snip--
#     except FileNotFoundError:
#       pass
#     else:
#       --snip--
