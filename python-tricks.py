import numpy as np

# array inversion
a = np.array([1, -2, 3, 4], dtype=int)
print(f"input array: {a}")
print(f"inverted array: {a[::-1]}")

# swap variables
x = 1
y = 2
print(f"Original: x = {x}, y = {y}")
x, y = y, x
print(f"Swapped: x = {x}, y = {y}")
