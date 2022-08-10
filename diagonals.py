size = int(input())
primary_sum = 0
primary = []
secondary_sum = 0
secondary = []
matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split(', ')])

for index in range(size):
    primary.append(matrix[index][index])
    primary_sum += matrix[index][index]
    secondary.append(matrix[index][size - index - 1])
    secondary_sum += matrix[index][size - index - 1]

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {secondary_sum}")
