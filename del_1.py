from math import exp

def calculate(x):
    # Function here
    return exp(x) / x

# Upper and lower limits
upper = 5
lower = 3

# parts = (upper - lower) * 100000
parts = (upper - lower) * 100000
width = (upper - lower) / parts

midpoint = lower + (width / 2)
area = 0
for _ in range(parts):
    area += calculate(midpoint) * width
    midpoint += width

print(area.__round__(8))