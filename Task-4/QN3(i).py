a = [[1, 'rishith', 83],
     [2, 'virat', 48],
     [3, 'abhiram', 99]]

print("{:<10} {:<10} {:<10}".format('Roll no', 'name', 'marks'))

for j in a:
    for b in j:
        print(b,end=" "*10)
    print()





