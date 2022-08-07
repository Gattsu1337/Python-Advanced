text = input()
dd = {}
for ch in text:
    if ch in dd.keys():
        dd[ch] += 1
    else:
        dd[ch] = 1

for key, value in sorted(dd.items()):
    print(f'{key}: {value} time/s')