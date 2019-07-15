import sys
from functools import lru_cache

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)

@lru_cache(maxsize = None)
def f(a, b, k):
    if not (a and b and k):
        return 0
    if a == b == 1:
        return 1
    return f((a + 1) // 2, (b + 1) // 2, (k + 1) // 2) + \
           f((a + 1) // 2, b // 2, (k + 1) // 2) + \
           f(a // 2, (b + 1) // 2, (k + 1) // 2) + \
           f(a // 2, b // 2, k // 2)

t = int(input())
for ti in range(1, t + 1):
    a, b, k = map(int, input().split())
    printf("Case #{}: {}".format(ti, f(a, b, k)))
