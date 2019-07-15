import sys


filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")

def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    a, b = map(int, input().split())
    p = list(map(float, input().split()))
    res = b + 2
    clean = 1.0
    for i, x in enumerate(p):
        clean *= x
        backspaces = a - i - 1
        res = min(res, backspaces * 2 + b - a + 1 + (b + 1) * (1 - clean))
    printf("Case #{}: {:0.6f}".format(ti, res))
