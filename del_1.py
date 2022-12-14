from math import exp

def calculate(x):
    return 5 + 2 * exp(-0.5*x)

upper = 9
lower = 1
parts = (upper - lower) * 100_000

area = 0
for i in range(parts):
    area += calculate(i) * i / parts

print(area.__round__(2))