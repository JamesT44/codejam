import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, l = map(int, input().split())
    o = list(int(x, 2) for x in input().split())
    d = set(int(x, 2) for x in input().split())
    res = 1e100
    for x in d:
        f = o[0] ^ x
        if set(ox ^ f for ox in o) == d:
            c = 0
            while f:
                c += 1
                f &= f - 1
            res = min(res, c)
    printf("Case #{}: {}".format(ti, res if res != 1e100 else "NOT POSSIBLE"))