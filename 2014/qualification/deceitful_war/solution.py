import sys

filename = "D-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    l = int(input())
    n = list(sorted(map(float, input().split())))
    k = list(sorted(map(float, input().split())))
    a = 0
    for i, x in enumerate(k):
        while i + a < l and n[i + a] < x:
            a += 1
    b = 0
    for i, x in enumerate(n):
        while i + b < l and k[i + b] < x:
            b += 1
    printf("Case #{}: {} {}".format(ti, l - a, b))
