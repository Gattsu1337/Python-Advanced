numbers = [int(k) for k in input().split()]
target = int(input())
answers = []
counter = 0

for i1 in range(len(numbers)):
    for i2 in range(i1 + 1, len(numbers)):
        p1 = numbers[i1]
        p2 = numbers[i2]
        if p1 + p2 == target:
            print(f"{p1} + {p2} = {target}")
            answers.append((numbers[i1], numbers[i2]))
        counter += 1
print(f"Iterations done: {counter}")
answers = set(answers)
for s in answers:
    print(s)