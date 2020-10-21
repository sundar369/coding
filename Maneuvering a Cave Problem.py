a = int(input())
b = int(input())

def calculate(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return calculate(a - 1, b) + calculate(a, b - 1)
print(calculate(a, b))