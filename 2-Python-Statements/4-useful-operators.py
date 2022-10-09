# range
# The range function allows you to quickly generate a list of integers, this comes in handy a lot, so take note of how to use it! There are 3 parameters you can pass, a start, a stop, and a step size. Let's see some examples:

print(range(0,11))

print(list(range(0,11)))

# Third parameter is step size!
# step size just means how big of a jump/leap/step you 
# take from the starting number to get to the next number.

print(list(range(0,11,2)))

# enumerate
# enumerate is a very useful function to use with for loops. Let's imagine the following situation:

# Notice the tuple unpacking!

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

# zip
# Notice the format enumerate actually returns, let's take a look by transforming it to a list()

print(list(enumerate('abcde')))

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
zip(mylist1,mylist2)
print(list(zip(mylist1,mylist2)))

# To use the generator, we could just use a for loop

for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))

# in operator
# We've already seen the in keyword during the for loop, but we can also use it to quickly check if an object is in a list

print('x' in ['x','y','z'])

print('x' in [1,2,3])

# not in
# We can combine in with a not operator, to check if some object or variable is not present in a list.

print('x' not in ['x','y','z'])
print('x' not in [1,2,3])


# min and max
# Quickly check the minimum or maximum of a list with these functions.

mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

# random
# Python comes with a built in random library. There are a lot of functions included in this random library, so we will only show you two useful functions for now.

from random import shuffle
# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
shuffle(mylist)
print(mylist)

from random import randint
# Return random integer in range [a, b], including both end points.
print(randint(0,100))

# Return random integer in range [a, b], including both end points.
print(randint(0,100))

# input
input('Enter Something into this box: ')