import sys
from math import log2, ceil, gcd

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    p, q = map(int, input().split("/"))
    g = gcd(p, q)
    p //= g
    q //= g
    if int(log2(q)) != log2(q):
        printf("Case #{}: impossible".format(ti))
    else:
        printf("Case #{}: {}".format(ti, ceil(log2(q / p))))
