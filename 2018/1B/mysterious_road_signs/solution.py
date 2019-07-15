import sys
#
# filename = "-small-practice"
# sys.stdin = open(filename + ".in", "r")
# sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    s = int(input())
    signs = [(d + a, d - b) for (d, a, b) in [map(int, input().split()) for _ in range(s)]]
    m, n = (*signs[0], 0, 0), (*signs[0], 0, 0)
    res = 1
    count = 1
    for i in range(1, s):
        a, b = signs[i]
        if a == signs[i - 1][0]:
            nm = m
        elif a == n[0]:
            nm = n[:3] + (i,)
        else:
            nm = (a, n[1], n[3], i)
        if b == signs[i - 1][1]:
            nn = n
        elif b == m[1]:
            nn = m[:3] + (i,)
        else:
            nn = (m[0], b, m[3], i)
        m, n = nm, nn
        x, y = i - m[2] + 1, i - n[2] + 1
        if x > res:
            res = x
            count = 0
        if y > res:
            res = y
            count = 0
        if x == res or y == res:
            count += 1
    printf("Case #{}: {} {}".format(ti, res, count))
