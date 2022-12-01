import math
from math import *

k = 0
for x in range(1, 100):
    for y in range(1, 100):
        if x < 12 and y < 12:
            if not((y >= x * tan(pi / 6)) and (y <= x * tan(pi / 6) + 8) and (x <= 8 * cos(pi / 6))):
                k += 1
print(k)