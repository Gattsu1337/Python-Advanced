from collections import deque

water_quantity = int(input())
command = input()
queue = deque()

while command != 'Start':
    queue.append(command)
    command = input()

new_command = input()
while new_command != 'End':
    if new_command.isdigit():

        if int(new_command) > water_quantity:
                print(f"{queue[0]} must wait")
                queue.popleft()
        else:
            water_quantity -= int(new_command)
            print(f"{queue[0]} got water")
            queue.popleft()

    else:
        refill = new_command.split()
        water_quantity += int(refill[1])
    new_command = input()
print(f"{water_quantity} liters left")