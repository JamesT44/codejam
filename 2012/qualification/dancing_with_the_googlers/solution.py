import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, s, p, *totals = map(int, input().split())
    res = 0
    for total in totals:
        k = (total + 2) // 3
        if k >= p:
            res += 1
        elif k == p - 1 and s and total % 3 != 1 and 2 <= total <= 28:
            s -= 1
            res += 1
    printf("Case #{}: {}".format(ti, res))
