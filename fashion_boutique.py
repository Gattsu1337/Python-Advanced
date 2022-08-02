clothes = [int(x) for x in input().split()]
capacity = int(input())
current_capacity = capacity
racks_counter = 1
while clothes:
    piece_of_clothing = clothes[-1]
    if piece_of_clothing > current_capacity:
        racks_counter += 1
        current_capacity = capacity
    else:
        current_capacity -= piece_of_clothing
        clothes.pop()
print(racks_counter)