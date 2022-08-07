n = int(input())
ss = set()
for _ in range(n):
    name = input()
    ss.add(name)

[print(x) for x in ss]