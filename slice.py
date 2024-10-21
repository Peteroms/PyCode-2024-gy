# Work through a specific group in a list.
# Specify the index of first and last element, as with range() function
players = ['peter', 'john', 'mark', 'james']
print(players[0:3])

# To work from begin of a list to a certain index
print(players[:2])

# To work from an index to the end of line
print(players[1:])

# Looping through a slice
print('This are my best players:')
for player in players[1:]:
    print(player.title())


# Copying a list, make a slice that includes entire original list
my_food = ['rice', 'chiken', 'nuts']
friends_food = my_food[:]
print(my_food)
print(friends_food)
