from random import randint
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 100
n = 100
print(tc)
for t in range(tc):
    wh = [randint(1, 250) for _ in range(n * 2)]
    p = randint(sum(wh) * 2, 10 ** 8)
    print(n, p)
    while wh:
        print(*wh[:2])
