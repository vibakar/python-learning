# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}

# Call values by their key
print(my_dict['key2'])

# Its important to note that dictionaries are very flexible in the data types they can hold. For example:
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# We can affect the values of a key as well. For instance:
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])

# Create a new dictionary
d = {}
# Create a new key through assignment
d['animal'] = 'Dog'
# Can do this with any object
d['answer'] = 42
#Show
print(d)

# Method to return a list of all keys 
print(d.keys())

# Method to grab all values
print(d.values())

# Method to return tuples of all items
print(d.items())
