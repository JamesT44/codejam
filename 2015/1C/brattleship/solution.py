import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    r, c, w = map(int, input().split())
    printf("Case #{}: {}".format(ti, c // w * r + w - (0 if c % w else 1)))
