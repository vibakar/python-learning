row1 = ['x','','x']

print(len(list(set(row1))))

if len(list(set(row1))) == 1 and row1[0] == 'x':
    print("All Same")
else:
    print("not Same")