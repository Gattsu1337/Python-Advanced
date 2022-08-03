stack = []
given_number = int(input())
for _ in range(given_number):
    query = [int(x) for x in input().split()]
    command = query[0]
    if command == 1:
        pushed_number = query[1]
        stack.append(pushed_number)
    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))