from math import floor
from collections import deque
number_queue = deque()
expression = input().split()
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: floor(a / b),
    '*': lambda a, b: a * b
}
for x in expression:
    if x in '/*+-':
        while len(number_queue) > 1:
            left = number_queue.popleft()
            right = number_queue.popleft()
            result = operations[x](left, right)
            number_queue.appendleft(result)

    else:
        number_queue.append(int(x))

print(number_queue[0])