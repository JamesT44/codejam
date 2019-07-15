import sys

filename = "C-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    c, d, v = map(int, input().split())
    pre = list(map(int, input().split()))
    res = 0
    n = 0
    while n < v:
        if pre and pre[0] <= n + 1:
            n += pre.pop(0) * c
        else:
            res += 1
            n += (n + 1) * c
    printf("Case #{}: {}".format(ti, res))
