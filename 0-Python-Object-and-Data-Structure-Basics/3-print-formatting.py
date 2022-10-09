# Formatting with placeholders

# You can use %s to inject strings into your print statements. The modulo % is referred to as a "string formatting operator".
print("I'm going to inject %s here" %'something')

# You can pass multiple items by placing them inside a tuple after the % operator.
print("I'm going to inject %s text here, and %s text here." %('some','more'))

# You can also pass variable names:
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))


# Formatting with the .format() method
print('This is a string with an {}'.format('insert'))

# Inserted objects can be called by index position:
print('The {2} {1} {0}'.format('fox','brown','quick'))

# Inserted objects can be assigned keywords:
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))


# Inserted objects can be reused, avoiding duplication:
print('A %s saved is a %s earned.' %('penny','penny'))
# vs.
print('A {p} saved is a {p} earned.'.format(p='penny'))


# Formatted String Literals (f-strings)
name = 'Fred'
print(f"He said his name is {name}.")

# Pass !r to get the string representation:
print(f"He said his name is {name!r}")

