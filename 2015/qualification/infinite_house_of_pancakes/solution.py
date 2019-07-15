import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    _= input()
    d = list(map(int, input().split()))
    res = max(d)
    for x in range(1, res):
        total = x
        for di in d:
            total += (di - 1) // x
        res = min(res, total)
    printf("Case #{}: {}".format(ti, res))