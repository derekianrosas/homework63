#zip function merge lists or multiple lists into tuples
#matrix is a set of nested collections
positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
#zip used to merge the lists together as an object and you can do what you wish with the object
# can also be converted into a dictionary
scoreboard = zip(positions, players)
print(dict(scoreboard))