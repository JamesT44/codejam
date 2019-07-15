import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, r, o, y, g, b, v = [int(x) for x in input().split(" ")]
    if o == y == b == v == 0 and r == g:
        printf("Case #{}: {}".format(ti, "RG" * r))
        continue
    if r == y == g == v == 0 and o == b:
        printf("Case #{}: {}".format(ti, "OB" * o))
        continue
    if r == o == g == b == 0 and y == v:
        printf("Case #{}: {}".format(ti, "YV" * y))
        continue
    if (g + 1 > r and g) or (v + 1 > y and v) or (o + 1 > b and o):
        printf("Case #{}: IMPOSSIBLE".format(ti))
        continue
    r -= g
    y -= v
    b -= o
    if r + y + b < max(r, y, b) * 2:
        printf("Case #{}: IMPOSSIBLE".format(ti))
        continue
    pri = sorted([["R", r], ["Y", y], ["B", b]], key=lambda x: x[1])
    aa, bb, cc, xx, yy, zz = pri[0][0], pri[1][0], pri[2][0], pri[0][1], pri[1][1], pri[2][1]
    out = ([cc, bb, aa] * (xx + yy - zz)) + ([cc, bb] * (zz - xx)) + ([cc, aa] * (zz - yy))
    if g:
        out.insert(out.index("R"), "RG" * g)
    if v:
        out.insert(out.index("Y"), "YV" * v)
    if o:
        out.insert(out.index("B"), "BO" * o)

    printf("Case #{}: {}".format(ti, "".join(out)))
