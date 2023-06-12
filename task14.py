import math
rad, height = input().split(", ")
rad = float(rad)
height = float(height)
pi = math.pi
v = pi * rad ** 2 * height
print(round(v, 2))
