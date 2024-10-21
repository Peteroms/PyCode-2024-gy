# Accessing elements in a list using index
cars = ['audi', 'mercedes', 'vox', 'toyota']
print(cars[0].title())

# Using individual values from a list
message = "My fist car was a " + cars[3].title() + "."
print(message)

# Modifying element in a list
cars[2] = 'tesla'
print(cars)

# Add element to a list using append() method...can be new data, registered user etc
cars.append('subaru')
print(cars)

# Add element using insert() method by specifying index position
cars.insert(0, 'mitsu')
print(cars)

# Remove an element from list by del if you know the position ...e.g del cars(1)# Remove an item from list and use the value of the item removed using pop() method
unused_car = cars.pop(3)
print(" I decided to drop " + unused_car + " due to fuel cosumption!")

# Remove an item from list by value using remove() method...e.g cars.remove(suzuki)
cars.insert(1, 'vox')
cars.remove('vox')
print(cars)

# Organize list in alphabetical order using sort() method
cars.sort()
print(cars)

# Organize list in reverse order using reverse() method
# Finding the length of a list using len() function i.e the no of items in a list
print(len(cars))

# Use index -1  to access the last item in list
print(cars[-1])

