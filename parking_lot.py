number_of_commands = int(input())
parking_lot_logs = [input().split(', ') for _ in range(number_of_commands)]
parking_lot = set()
for direction, car_number in parking_lot_logs:
    if direction == 'IN':
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)

if not parking_lot:
    print('Parking Lot is Empty')
else:
    [print(car_number) for car_number in parking_lot]