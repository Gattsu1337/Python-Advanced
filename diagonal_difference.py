size = int(input())
matrix = []


def get_matrix(matrix, size):
    for _ in range(size):
        matrix.append([int(x) for x in input().split()])
    return matrix


def primary_diagonal(matrix, size):
    primary_sum = 0
    primary = []
    for index in range(size):
        primary.append(matrix[index][index])
        primary_sum += matrix[index][index]
    return primary_sum


def secondary_diagonal(matrix, size):
    secondary_sum = 0
    secondary = []
    for index in range(size):
        secondary.append(matrix[index][size - index - 1])
        secondary_sum += matrix[index][size - index - 1]
    return secondary_sum


def abs_difference(primary_sum, secondary_sum):
    return abs(primary_sum - secondary_sum)


get_matrix(matrix, size)
print(abs_difference(primary_diagonal(matrix, size), secondary_diagonal(matrix, size)))
