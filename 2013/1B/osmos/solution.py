import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    a, n = map(int, input().split())
    m = list(sorted(map(int, input().split())))
    if a == 1:
        printf("Case #{}: {}".format(ti, n))
        continue
    while m and m[0] < a:
        a += m.pop(0)
    res = len(m)
    curr = 0
    while m:
        while a <= m[0]:
            curr += 1
            a += a - 1
        while m and m[0] < a:
            a += m.pop(0)
        res = min(res, curr + len(m))
    printf("Case #{}: {}".format(ti, res))