from collections import deque

worker_bees = deque([int(x) for x in input().split()])
nectar_int = [int(x) for x in input().split()]
operators = deque(input().split())

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b

}

total_honey = 0

while worker_bees and nectar_int:
    bee = worker_bees.popleft()
    nectar = nectar_int.pop()

    if nectar < bee:
        worker_bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operator = operators.popleft()

    total_honey += abs(operations[operator](bee, nectar))

print(f'Total honey made: {total_honey}')

if worker_bees:
    print(f'Bees left: {", ".join([str(x) for x in worker_bees])}')
if nectar_int:
    print(f'Bees left: {", ".join([str(x) for x in nectar_int])}')