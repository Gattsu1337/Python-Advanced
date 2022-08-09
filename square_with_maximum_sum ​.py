paras = [int(x) for x in input().split(', ')]
rows, cols = paras[0], paras[1]
matrix = []
for row in range(rows):
    row_elements = input().split(', ')
    matrix.append(row_elements)

biggest_square = 0
for row in matrix:
    for col in row:
        print(matrix[row][col])

print(matrix)