#tuples are ordered collections of items that are immuatble.
#they are similar to lists

# An empty tuple
empty_tuple = ()

# A tuple with elements
my_tuple = (1, 'apple', 3.14, (2, 'banana'), [4, 5, 6],1)


print(my_tuple[1])  # Output: apple
print(my_tuple[3][1])  # Output: banana

#u cannot modify their elements
# This will raise a TypeError
my_tuple[0] = 2


print(my_tuple[1:3])  # Output: ('apple', 3.14)

#tuple operation


''''Tuple vs List
Tuples are immutable, making them faster and suitable for fixed data.

Lists are mutable and more flexible for dynamic data. '''

#tuple methods
print(my_tuple.count(1)) #2
print(my_tuple.index('apple')) #1

#packing and unpacking tuple
packed_tuple= 1, 'hi', 6.8
print(packed_tuple)

# Tuple unpacking
a, b, c, d = my_tuple
print(a, b, c, d)  # Output: 1 hello 3.14 (2, 'world')

