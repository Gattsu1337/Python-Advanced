n = int(input())
my_set = set()
for a in range(n):
    [my_set.add(b) for b in input().split()]
[print(d) for d in my_set]