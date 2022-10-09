x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    
else:
    print('All Done!')

print("###################")

# break, continue, pass
# We can use break, continue, and pass statements in our loops to add additional functionality for various cases. The three statements are defined by:

# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all.

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
        break