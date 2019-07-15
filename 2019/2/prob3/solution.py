from math import inf
from fractions import Fraction


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


def cf(n, d):
    res = []
    while n and d:
        q, r = n // d, n % d
        res.append(q)
        d, n = r, d
    return res

t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    pairs = [tuple(map(int, input().split())) for _ in range(n)]
    rel = 0
    lb, ub = Fraction(0, 1), inf
    for (ca, ja), (cb, jb) in zip(pairs[:-1], pairs[1:]):
        cd, jd = cb - ca, jb - ja
        if cd <= 0 and jd <= 0:
            printf("Case #{}: IMPOSSIBLE".format(ti))
            break
        if cd and jd:
            if cd < 0:
                f = Fraction(jd, -cd)
                ub = min(ub, f)
            elif jd < 0:
                f = Fraction(-jd, cd)
                lb = max(lb, f)
    else:
        if lb >= ub:
            printf("Case #{}: IMPOSSIBLE".format(ti))
        else:
            if ub == inf:
                printf("Case #{}: {} {}".format(ti, int(lb) + 1, 1))
                continue
            lcf, ucf = cf(lb.numerator, lb.denominator), cf(ub.numerator, ub.denominator)
            ll, ul = len(lcf), len(ucf)
            if ll < ul:
                ll.append(inf)
            elif ul < ll:
                ul.append(inf)
            res = []
            for l, u in zip(lcf, ucf):
                if l != u:
                    res.append(min(l, u) + 1)
                    break
                else:
                    res.append(l)
            a = Fraction(0)
            for x in res[:0:-1]:
                a = 1 / (x + a)
            printf("Case #{}: {} {}".format(ti, a.denominator, a.numerator + res[0] * a.denominator))
