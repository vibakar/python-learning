# Assign a list to an variable named my_list
a = [1,2,3]

# We just created a list of integers, but lists can actually hold different object types. For example:
b = ['A string',23,100.232,'o']

print(len(b))

# Grab element at index 0
print(b[0])

# Grab index 1 and everything past it
print(b[1:])

# Make the list double
print(b * 2)

# Append
b.append('append me!')
print(b)

# Pop off the 0 indexed item
b.pop(0)
print(b)

# Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
new_list = ['c', 'b', 'x', 'e', 'a']
new_list.sort()
print(new_list)

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
print(matrix)

# Grab first item in matrix object
print(matrix[0])

# Grab first item of the first item in the matrix object
print(matrix[0][0])

first_col = [row[0] for row in matrix]
print(first_col)