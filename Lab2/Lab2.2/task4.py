def transpose(matrix):
    row_length = len(matrix[0])
    column_length = len(matrix)
    transp_matrix = [[matrix[i][j] for i in range(column_length)] for j in range(row_length)]
    return transp_matrix


n, m = map(int, input("Enter size of matrix: ").split())
print("Enter matrix: ")
matrix = [val for val in range(m)]
for i in range(n):
    matrix[i] = list(map(int, input("").split()))
print(matrix)

transp_matrix = transpose(matrix)

print("Matrix:")
for row in matrix:
    print(row)

print("\nTranspose matrix:")
for row in transp_matrix:
    print(row)