# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
print("########### lesser_of_two_evens: ###########")

def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(2, 5))
print(lesser_of_two_evens(2, 5))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
print("########### animal_crackers: ###########")

def animal_crackers(words):
    list = words.split()
    if list[0][0] == list[1][0]:
        return True
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers("Crazy Kangaroo"))

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
print("########### makes_twenty: ###########")

def makes_twenty(n1,n2):
    if (n1+n2 == 20) or (n1 == 20) or (n2 == 20):
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
print("########### old_macdonald: ###########")

def old_macdonald(word):
    result = ""
    for index,letter in enumerate(word):
        if index == 0 or index == 3:
            result+= letter.upper()
        else:
            result+= letter
    
    print(result)

old_macdonald('macdonald')

# MASTER YODA: Given a sentence, return a sentence with the words reversed
print("########### master_yoda: ###########")

def master_yoda(sentence):
    result = []
    words = sentence.split(" ")
    for word in range(len(words)):
        result.append(words.pop())
    print(" ".join(result))

master_yoda('I am home')
master_yoda('We are ready')

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
print("########### almost_there: ###########")

def almost_there(n):
    if(abs(100 - n) <= 10 or abs(200 - n) <= 10):
        print("True")
    else:
        print("False")

almost_there(90)
almost_there(104)
almost_there(150)
almost_there(209)

# LEVEL 2 PROBLEMS
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
print("########### has_33: ###########")

def has_33(list):
    for i in range(0, len(list) - 1):
        if(list[i] == 3 and list[i + 1] == 3):
            print("True")
            return True
    
    print("False")
    return False

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
print("########### paper_doll: ###########")

def paper_doll(str):
    result = ""
    for letter in str:
        result+= letter*3
    
    print(result)

paper_doll('Hello')
paper_doll('Mississippi')


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
print("########### BLACKJACK: ###########")

def blackjack(a,b,c):
    total = a + b + c
    if total <= 21:
        return total
    elif total > 21: 
        if a == 11 or b == 11 or c == 11:
            new_total = total - 10
            if new_total > 21:
                return "BUST"
            else:
                return new_total
        else:
            return "BUST"

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
#  Return 0 for no numbers.
print("########### SUMMER OF 69: ###########")

def summer_69(arr):
    total = 0
    found_6 = False

    for num in arr:
        if num == 6:
            found_6 = True
        if num == 9:
            found_6 = False
            continue
        if found_6 == False:
            total+= num
    
    print(total)


summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])

# CHALLENGING PROBLEMS
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
print("########### spy_game: ###########")

def spy_game(arr):
    find_nums = [0, 0, 7]
    nums_index = []
    for n in find_nums:
        for index,input_num in enumerate(arr):
            if n == input_num:
                nums_index.append(index)
                arr[index] = "_"
        
    if(len(nums_index) == 3):
        if nums_index[0] < nums_index[1] < nums_index[2]:
            return True
        else:
            return False
    else:
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# By convention, 0 and 1 are not prime.
print("########### COUNT PRIMES: ###########")
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))


# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
print("########### PRINT BIG: ###########")
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('E')
