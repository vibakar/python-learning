file = open("1-numbers.py", "r")
# We can now read the file
print(file.read())
# But what happens if we try to read it again?
print(file.read()) # output will be empty

# This happens because you can imagine the reading "cursor" is at the end of the file after having read it. So there is nothing left to read. We can reset the "cursor" like this:
# Seek to the start of file (index 0)
file.seek(0)
# Now read again
print(file.read())

# Readlines returns a list of the lines in the file
file.seek(0)
print(file.readlines())

file.close()

print("################################################")
# Writing to a File
# By default, the open() function will only allow us to read the file. We need to pass the argument 'w' to write over the file. For example:

# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

new_file = open('test.txt','w+')
# Opening a file with 'w' or 'w+' truncates the original, meaning that anything that was in the original file is deleted!

# Write to the file
new_file.write('This is a new line')

# Read the file
new_file.seek(0)
print(new_file.read())

new_file.close()  # always do this when you're done with a file

print("################################################")
# Appending to a File
# Passing the argument 'a' opens the file and puts the pointer at the end, so anything written is appended. Like 'w+', 'a+' lets us read and write to a file. If the file does not exist, one will be created.

my_file = open('test.txt','a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')

my_file.seek(0)
print(my_file.read())
my_file.close()

print("################################################")
# Iterating through a File
# Now we can use a little bit of flow to tell the program to for through every line of the file and do something:

for line in open('test.txt'):
    print(line)

#It's important to note a few things here:

#We could have called the "line" object anything (see example below).
#By not calling .read() on the file, the whole text file was not stored in memory.
