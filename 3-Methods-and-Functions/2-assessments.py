from operator import truediv
import string

# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as 4/3 pie r cube
print("########## vol: ##########")

def vol(rad):
    print((4/3)*3.14*(rad**3))

vol(2)

# Write a function that checks whether a number is in a given range (inclusive of high and low)
print("########## ran_check: ##########")

def ran_check(num,low,high):
    if num in range(low, high):
        print(f"{num} is in the range between {low} and {high}")
    else:
        print(f"{num} is not in the range between {low} and {high}")

ran_check(5,2,7)


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
print("########## up_low: ##########")

def up_low(s):
    lower_count = 0
    upper_count = 0
    for letter in s:
        if letter.isupper():
            lower_count+= 1
        if letter.islower():
            upper_count+= 1
    
    print(f"No. of lower case characters : {lower_count} \n No. of Upper case characters : {upper_count}")

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
print("########## up_low: ##########")

def unique_list(lst):
    print(list(set(lst)))

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24
print("########## multiply: ##########")

def multiply(numbers):
    result = 1
    for num in numbers:
        result*= num
    return result

print(multiply([1,2,3,-4]))

# Write a Python function that checks whether a word or phrase is palindrome or not.
print("########## palindrome: ##########")
def palindrome(s):
    reversed_str = s[::-1]
    if s == reversed_str:
        return True
    else:
        return False

print(palindrome('helleh'))

# Hard:
# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
print("########## Pangrams: ##########")

def ispangram(str1, alphabets=string.ascii_lowercase):
    alphabets = list(alphabets)
    str = str1.lower().replace(" ", "")
    
    for letter in alphabets:
        if letter not in str:
            return False
    return True

print(ispangram("The quick brown fox jumps over the lazy dog"))