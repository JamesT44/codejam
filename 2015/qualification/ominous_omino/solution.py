import sys

filename = "D-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    x, r, c = map(int, input().split())
    if r > c:
        r, c = c, r
    if (r * c) % x or (x > 2 and (x + 2) // 2 > r) or (x, r, c) == (5, 3, 5) or x >= 7:
        printf("Case #{}: RICHARD".format(ti, 0))
    else:
        printf("Case #{}: GABRIEL".format(ti, 0))