a = [[1, 'rishith', 83],
     [2, 'virat', 48],
     [3, 'abhiram', 99]]

print("{:<10} {:<10} {:<10}".format('Roll no', 'name', 'marks'))

for j in range(3):
    print(a[1][j],end=" " * 10)
