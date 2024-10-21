# Tuples are a list of items that are immutable, i.e they cannot change
# Define a tuple using parenthesis ()
dimensions = (150, 50)
print(dimensions[0])
print(dimensions[1])

# Trying to change an item e.g dimensions[0] = 200, an error message will be returned

# Loop through all values in a Tuple just the way you did in a list
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple; assign new values to a variable that holds a tuple
rectangles = (200, 120)
print('Original size')
for rectangle in rectangles:
    print(rectangle)

rectangles = (1000, 700)
print('\nNew size')
for rectangle in rectangles:
    print(rectangle)

