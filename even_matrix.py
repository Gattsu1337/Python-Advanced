'''
n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])

print(matrix)
'''

n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
print([[x for x in row if x % 2 == 0] for row in matrix])
