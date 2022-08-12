def get_next_pos(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    else:
        return row, col + 1


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_around_kids(matrix, row, col):
    result = []
    if is_inside(row, col - 1, len(matrix)) and matrix[row][col - 1] == 'X' or matrix[row][col - 1] == 'V':
        result.append([row, col - 1])
    if is_inside(row, col + 1, len(matrix)) and matrix[row][col + 1] == 'X' or matrix[row][col + 1] == 'V':
        result.append([row, col + 1])
    if is_inside(row - 1, col, len(matrix)) and matrix[row - 1][col] == 'X' or matrix[row - 1][col] == 'V':
        result.append([row - 1, col])
    if is_inside(row + 1, col, len(matrix)) and matrix[row + 1][col] == 'X' or matrix[row + 1][col] == 'V':
        result.append([row + 1, col])

    return result


presents = int(input())
size = int(input())
matrix = []
santa_row, santa_col = 0, 0
nice_kids = 0
nice_kids_gifted = 0
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'S':
            santa_row, santa_col = row, col
        elif row_elements[col] == 'V':
            nice_kids += 1
    matrix.append(row_elements)


while presents > 0:
    line = input()
    if line == "Christmas morning":
        break
    matrix[santa_row][santa_col] = '-'
    santa_row, santa_col = get_next_pos(santa_row, santa_col, line)

    if matrix[santa_row][santa_col] == 'V':
        presents -= 1
        nice_kids_gifted += 1
    elif matrix[santa_row][santa_col] == 'C':
        around_kids = get_around_kids(matrix, santa_row, santa_col)
        for kid_row, kid_col in around_kids:
            if matrix[kid_row][kid_col] == 'V':
                nice_kids_gifted += 1
            presents -= 1
            matrix[kid_row][kid_col] = '-'
            if presents == 0:
                break
    matrix[santa_row][santa_col] = 'S'

if presents == 0 and nice_kids != nice_kids_gifted:
    print("Santa ran out of presents!")
for row in matrix:
    print(*row, sep=' ')
if nice_kids_gifted == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f'No presents for {nice_kids - nice_kids_gifted} nice kid/s.')