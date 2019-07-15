import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for x in sorted(a):
        n -= 1
        xi = a.index(x)
        res += min(xi, n - xi)
        a.pop(xi)
    printf("Case #{}: {}".format(ti, res))