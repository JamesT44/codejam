import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    c, f, x = map(float, input().split())
    res = x / 2
    k = 1
    ft = c / 2
    while x / (k * f + 2) + ft < res:
        res = x / (k * f + 2) + ft
        ft += c / (2 + k * f)
        k += 1
    printf("Case #{}: {:0.7f}".format(ti, res))