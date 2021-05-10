'''
Tuples - used to store info like list but are immutable(unchangeable)

numbers = (1, 2, 3)
print(numbers[0])

cannot change already set tuples
numbers[0] = 3 not allowed
'''

coordinates = (1, 2, 3)
'''
coordinates[0] * coordinates[1] * coordinates [2]
a lot going on above, so better to use variables for long items,
or items that will come up more often

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
Better, but still unnecessary amount of code
Use unpacking: x, y, z = 1, 2, 3
'''
x, y, z = coordinates
print(x)