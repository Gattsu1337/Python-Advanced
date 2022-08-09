matrix = []
rows = int(input())
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

print([x for row in matrix for x in row])