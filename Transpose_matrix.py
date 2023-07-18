def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transposed = []
    for _ in range(columns):
        row = []
        for _ in range(rows):
            row.append(0)
        transposed.append(row)

    for i in range(rows):
        for j in range(columns):
            transposed[j][i] = matrix[i][j]
    return transposed
matrix = []
rows,columns=map(int,input().split())
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
transposed_matrix = transpose_matrix(matrix)
print("Transpose Matrix")
for row in transposed_matrix:
    print(*row)
