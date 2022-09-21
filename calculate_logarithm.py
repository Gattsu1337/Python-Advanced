from math import log
value = int(input())
base = int(input())
formatted_log = f'{log(value, base):.2f}'
print(formatted_log)