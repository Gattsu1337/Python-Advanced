size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input().split()

    if line[0] == 'END':
        break
    command = line[0]
    row, col, value = [int(x) for x in line[1:]]
    if 0 > row or row >= size or 0 > col or col >= size:
        print("Invalid coordinates")
        continue

    if command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=' ')