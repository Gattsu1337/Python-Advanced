def operate(operator, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    def divide(x, *args):
        result = x
        for a in args:
            result /= a
        return result

    if operator == '+':
        return add(*args)
    elif operator == '-':
        return subtract(*args)
    elif operator == '*':
        return multiply(*args)
    elif operator == '/':
        return divide(*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 1, 2, 3))
print(operate("/", 3, 4, 2, 3))