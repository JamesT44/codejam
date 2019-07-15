import sys
import math
from math import asin, sin, pi


filename = "C-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


n = int(input())
for ni in range(1, n + 1):
    f, R, t, r, g = map(float, input().split())
    a = r + f
    b = g + 2 * r
    c = g - 2 * f
    c2 = c * c
    d = R - t - f
    d2 = d * d
    res = 0
    x = a
    if c <= 1e-10:
        printf("Case #{}: 1.000000".format(ni))
        continue
    while True:
        y = a
        if x * x + y * y >= d2:
            break
        while y <= x:
            xx, yy = x + c, y + c
            x2, y2, xx2, yy2 = x * x, y * y, xx * xx, yy * yy
            gap = 0
            if xx2 + yy2 <= d2:
                gap = c2
            elif xx2 + y2 <= d2:
                ix, iy = (d2 - yy2) ** 0.5, (d2 - xx2) ** 0.5
                gap += (iy - y + ix - x) * c / 2
                gap += abs(x * (iy - yy) + xx * (yy - y) + ix * (y - iy)) / 2
                l = ((ix - xx) ** 2 + (iy - yy) ** 2) ** 0.5
                theta = asin(l / 2 / d) * 2
                gap += d2 / 2 * (theta - sin(theta))
            elif x2 + yy2 <= d2:
                i1, i2 = (d2 - yy2) ** 0.5, (d2 - y2) ** 0.5
                gap += c * (i1 + i2 - x - x) / 2
                l = (c2 + (i2 - i1) ** 2) ** 0.5
                theta = asin(l / 2 / d) * 2
                gap += d2 / 2 * (theta - sin(theta))
            elif x2 + y2 <= d2:
                ix, iy = (d2 - y2) ** 0.5, (d2 - x2) ** 0.5
                gap += (ix - x) * (iy - y) / 2
                l = ((ix - x) ** 2 + (iy - y) ** 2) ** 0.5
                theta = asin(l / 2 / d) * 2
                gap += d2 / 2 * (theta - sin(theta))
            else:
                break
            if x != y:
                res += gap
            res += gap
            y += b
        x += b
    printf("Case #{}: {:0.6f}".format(ni, 1 - (4 * res / (pi * R * R))))
