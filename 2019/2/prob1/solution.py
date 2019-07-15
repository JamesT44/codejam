from itertools import permutations
from math import inf

def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    pairs = [tuple(map(int, input().split())) for _ in range(n)]
    res = 0
    for order in permutations(pairs):
        lb, ub = 0, inf
        for (ca, ja), (cb, jb) in zip(order[:-1], order[1:]):
            cd, jd = cb - ca, jb - ja
            if cd <= 0 and jd <= 0:
                break
            if cd and jd:
                if cd < 0:
                    f = jd / -cd
                    ub = min(ub, f)
                elif jd < 0:
                    f = -jd / cd
                    lb = max(lb, f)
        else:
            res += lb < ub
    printf("Case #{}: {}".format(ti, res))
