def transpose(matrix):
    row_length = len(matrix[0])
    column_length = len(matrix)
    transp_matrix = [[matrix[i][j] for i in range(column_length)] for j in range(row_length)]
    return transp_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transp_matrix = transpose(matrix)

print("Matrix:")
for row in matrix:
    print(row)

print("\nTranspose matrix:")
for row in transp_matrix:
    print(row)