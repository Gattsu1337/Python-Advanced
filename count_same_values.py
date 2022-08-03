numbers_string = input().split()
numbers = [float(x) for x in numbers_string]
dd = {}
for number in numbers:
    if number not in dd.keys():
        dd[number] = 0
    dd[number] += 1

for number, value in dd.items():
    print(f'{number:.1f} - {value} times')
