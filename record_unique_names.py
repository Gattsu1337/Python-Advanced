names_set = set()
names_number = int(input())
for number in range(names_number):
    names_set.add(input())
[print(name) for name in names_set]