a = "Learning Python"

# Print the object
print(a)


print(type(a))

# We can also use a function called len() to check the length of a string!
print(len(a))

# Show first element (in this case a letter)
print(a[0])

# Grab everything past the first term all the way to the length of s which is len(s)
print(a[1:])

# Grab everything UP TO the 3rd index
print(a[:3])

#Everything
print(a[:])

# Last letter (one index behind 0 so it loops back around)
print(a[-1])

# Grab everything but the last letter
print(a[:-1])

# Grab everything, but go in steps size of 1
print(a[::1])

# We can use this to print a string backwards
print(a[::-1])

# Concatenate strings! We can reassign a completely though!
a = a + ' Happily!!'
print(a)

# We can use the multiplication symbol to create repetition!
letter = 'z'
print(letter*10)

# Upper Case a string
print(a.upper())

# Lower Case a string
print(a.lower())

# Split a string by blank space (this is the default)
print(a.split(' '))
