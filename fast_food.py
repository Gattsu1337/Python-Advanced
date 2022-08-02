from collections import deque
food_quantity = int(input())
orders = [int(x) for x in input().split()]
orders_queue = deque(orders)
biggest_order = max(orders_queue)
print(biggest_order)
while orders_queue:
    current_order = orders_queue[0]
    if current_order <= food_quantity:
        food_quantity -= current_order
        orders_queue.popleft()
    else:
        break
if not orders_queue:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(list(str(x) for x in orders_queue))}")
