sparse_matrix = []
print('Enter the entries rowise:')
for i in range(4):
    a = []
    for j in range(5):
        a.append(int(input()))
    sparse_matrix.append(a)

size = 0
for i in range(4):
    for j in range(5):
        if sparse_matrix[i][j] != 0:
            size += 1

rows, cols = 3, size
Matrix = [[0 for i in range(cols)] for j in range(rows)]
k = 0
for i in range(4):
    for j in range(5):
        if sparse_matrix[i][j] != 0:
            Matrix[0][k] = i
            Matrix[1][k] = j
            Matrix[2][k] = sparse_matrix[i][j]
            k += 1

print('Sparse Matrix:')
for i in range(3):
    for j in range(size):
        print(Matrix[i][j], end=' ')
    print()
