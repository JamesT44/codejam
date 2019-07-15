import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    _, shy = input().split()
    total = int(shy[0])
    res = 0
    for i, n in enumerate(shy[1:]):
        x = i + 1 - total
        n = int(n)
        if n and x > 0:
            res += x
            total += x
        total += n
    printf("Case #{}: {}".format(ti, res))