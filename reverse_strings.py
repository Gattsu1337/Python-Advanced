original_string = input()
s = []
for ch in original_string:
    s += ch
reversed_string = ''
while s:
    reversed_string += s.pop()
print(reversed_string)