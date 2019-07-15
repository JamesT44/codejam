import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    b, n = map(int, input().split())
    m = list(map(int, input().split()))
    if n <= b:
        printf("Case #{}: {}".format(ti, n))
        continue
    l, h = 0, max(m) * n
    while l + 1 < h:
        c = (h + l) // 2
        served = 0
        for mi in m:
            served += c // mi + 1
        if served < n:
            l = c
        else:
            h = c

    left = n
    for mi in m:
        left -= (h - 1) // mi + 1
    for i in range(b):
        if not h % m[i]:
            left -= 1
            if not left:
                printf("Case #{}: {}".format(ti, i + 1))
                break
