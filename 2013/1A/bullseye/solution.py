import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    r, c = map(int, input().split())
    b = 2 * r - 1
    res = int((-b + ((b * b + 8 * c) ** 0.5)) // 4)
    while res * (2 * res + 2 * r - 1) < c:
        res += 1
    while res * (2 * res + 2 * r - 1) > c:
        res -= 1
    printf("Case #{}: {}".format(ti, res))