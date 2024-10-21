# Use the range() function to print a series of numbers
for value in range(1,5):
    print(value)

# Use the range() function to make list of numbers
numbers = list(range(1,10))
print(numbers)

# To skip numbers in a range of values i.e even or add numbers
even_numbers = list(range(0,17,2))
odd_numbers = list(range(1,16,2))
print(even_numbers)
print(odd_numbers)

# Getting squares of a range of numbers
squares = []
for value in range(10,20):
    square = value**2  # or skip this line by directly writing;  squares.append(value**2)
    squares.append(square)
print(squares)

# Simple statistics with a list of numbers
digits = [145,12,3,19,34,98,1,57]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension; generate a list with few lines of code
cubes = [value**3 for value in range(1,10)] # Note, there is no colon
print(cubes)

# Use for loop to get a list of odd numbers
odd_numbers = [number for number in range(1,20,2)]
print(odd_numbers)

# Use for loop to get multiples of 3
multiple_3 = [num for num in range(3,31,3)]
print(multiple_3)
