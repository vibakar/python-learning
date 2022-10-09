# Grab every letter in string
lst = [x for x in 'word']
print(lst)

# Square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]
print(lst)

# Let's see how to add in if statements:
# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]
print(lst)

# Can also do more complicated arithmetic:
# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
print(fahrenheit)

# We can also perform nested list comprehensions, for example:
lst = [ x**2 for x in [x**2 for x in range(11)]]
lst