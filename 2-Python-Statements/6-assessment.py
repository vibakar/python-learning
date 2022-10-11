# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

for s in st.split(" "):
    if(s.startswith("s")):
        print(s)

# Use range() to print all the even numbers from 0 to 10.
for num in range(0, 10):
    if(num%2 == 0):
        print(num)

# Simplest answer below
print(list(range(0,11,2)))


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
divisible_by_three = [d for d in range(1, 50) if d%3 == 0]
print(divisible_by_three)

# Go through the string below and if the length of a word is even print "even!"
st1 = 'Print every word in this sentence that has an even number of letters'
even_len_words = [e for e in st1.split(" ") if(len(e)%2 == 0 )]
print(even_len_words)

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for n in range(1, 100):
    if ((n%3 ==0) and (n%5 == 0)):
        print("FizzBuzz")
    elif (n%3 == 0):
        print("Fizz")
    elif (n%5 == 0):
        print("Buzz")
    else:
        print(n)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st2 = 'Create a list of the first letters of every word in this string'

first_letters = [l[0] for l in st2.split(" ")]
print(first_letters)