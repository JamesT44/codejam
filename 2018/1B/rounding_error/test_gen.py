from random import randint
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 100
print(tc)
for t in range(tc):
    n = randint(10 ** 5 - 100, 10 ** 5)
    c = []
    x = n
    while x:
        c.append(randint(1, x))
        x -= c[-1]
    print(n, len(c) - 1)
    print(*c[1:])
