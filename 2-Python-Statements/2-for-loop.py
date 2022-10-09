list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)

for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')

# Start sum at zero
list_sum = 0 

for num in list1:
    list_sum += num

print(list_sum)


for letter in 'This is a string.':
    print(letter)


#Let's now look at how a for loop can be used with a tuple:
tup = (1,2,3,4,5)
for t in tup:
    print(t)

# Now with unpacking!
list2 = [(2,4),(6,8),(10,12)]
for (t1,t2) in list2:
    print(t1)


d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)


# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v)

print(list(d.keys()))
print(sorted(d.values()))
