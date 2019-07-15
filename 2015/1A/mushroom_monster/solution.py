import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    m = list(map(int, input().split()))
    x = 0
    mdiff = 0
    for i in range(n - 1):
        diff = m[i] - m[i + 1]
        if diff > 0:
            x += diff
        mdiff = max(mdiff, diff)
    y = sum(min(mi, mdiff) for mi in m[:-1])
    printf("Case #{}: {} {}".format(ti, x, y))