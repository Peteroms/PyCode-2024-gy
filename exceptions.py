# Codes that Manage errors that arise during a program execution.
# Exceptions are handled with try-except blocks. A try-except block asks Python to do sth, but it also tells Python what to do if an exception is raised.
# Tracebacks, which can be confusing to read, users will see friendly error messages that you write
# Example 1
try:                # If code in try block works,Python skips over the except block
    print(5/0)
except ZeroDivisionError:    
    print("Cant divide by zero")

# If more code followed the try-except block, the program will continue running.
# Example 2
print("Give me two numbers, let me Divide!")
print("Enter 'q' to exit")
while True:
    First_number = input("Enter first number")
    if First_number == 'q':
        break

    Second_number = input("Enter second number")
    if Second_number == 'q':
        break

    try:
        results = int(First_number) / int(Second_number)
        
    except ZeroDivisionError:
        print("not divisible")

    else:          # If try block has no error, any code dependent on the block is added to the else block. If try block has exception, we print a friendly message, program continues to run.
        print(results)

## Handling the FileNotFoundError Exception
# Example 1: Lets try to read from a file that doesnt exist, put the open() fucntion in a try block
filename = 'twit.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    message = 'Sorry ' + ' , your file is missing!'

    print(message)

    
