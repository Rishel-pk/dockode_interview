
a = int(input('enter row number'))
b = int(input('enter column number'))

matrix = [[0 for x in range(b)] for y in range(a)]

counter = 1

for k in range(b+a-1):
    for j in range(k+1):
        i = k-j

        if (i < a and j < b):
            matrix[i][j] = counter
            counter += 1

for i in range(a):
    for j in range(b):
        print(matrix[i][j], end=" ")
    print()
