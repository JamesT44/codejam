import sys
from math import ceil

# filename = "-small-practice"
# sys.stdin = open(filename + ".in", "r")
# sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    hd, ad, hk, ak, b, d = map(int, input().split())
    if ad < hk and ak - d >= hd:
        printf("Case #{}: {}".format(ti, "IMPOSSIBLE"))
        continue
    buffs = int((b * hk) ** 0.5 - ad)
    if buffs < 0:
        buffs = 0
    elif ceil(hk / (ad + b * buffs)) < 1 + ceil(hk / (ad + b * buffs + b)):
        buffs += 1
    m = buffs + ceil(hk / (ad + b * buffs))
    res = 1e100
    hi = hd
    if m <= (hd - 1) // ak + 1:
        res = m
    elif not d:
        u = (hd - ak - 1) // ak
        if u > 0 or hk <= ad:
            w = m - (hd - 1) // ak
            res = (hd - 1) // ak + w + (w + u - 2) // u
    elif not(hk > ad and ak - d >= hd):
        dt = 0
        pheal = False
        pu = -1
        while ak > 0:
            u = (hd - ak - 1) // ak
            if m <= (hi - 1) // ak + 1:
                res = min(res, m + dt)
            elif u > 0 and not pheal and u != pu:
                w = m - (hi - 1) // ak
                res = min(res, dt + (hi - 1) // ak + w + (w + u - 2))
            if hi <= ak -d:
                if pheal:
                    break
                dt += 1
                pheal = True
                hi = hd - ak
            else:
                pheal = False
                dt += 1
                ak -= d
                hi -= ak
            pu = u
        if ak <= 0:
            res = min(res, m + dt)
    printf("Case #{}: {}".format(ti, res if res != 1e100 else "IMPOSSIBLE"))
