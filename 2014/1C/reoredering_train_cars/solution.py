import sys
from collections import defaultdict
from math import factorial

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    singles, starts, ends, middles, endl = defaultdict(int), dict(), dict(), set(), dict()
    fail = False
    for i, car in enumerate(input().split()):
        collapsed = [car[0]]
        for c in car[1:]:
            if c != collapsed[-1]:
                collapsed.append(c)
        if len(collapsed) == 1:
            singles[collapsed[0]] += 1
        else:
            start, middle, end = collapsed[0], collapsed[1:-1], collapsed[-1]
            if start in middles or start in starts or end in middles or end in ends or start == end or start in middle or end in middle:
                fail = True
                break
            for c in middle:
                if c in starts or c in middles or c in ends or c in singles:
                    fail = True
                    break
            else:
                starts[start] = i
                ends[end] = i
                endl[i] = end
                middles.update(middle)
    if fail:
        printf("Case #{}: 0".format(ti))
    else:
        res = 1
        groups = 0
        for c, count in singles.items():
            res *= factorial(count)
            if c not in starts and c not in ends:
                groups += 1
        rem = set(starts.values())
        for start in (starts.keys() - ends.keys()):
            rem.remove(starts[start])
            end = endl[starts[start]]
            while end in starts:
                rem.remove(starts[end])
                end = endl[starts[end]]
            if end == start:
                printf("Case #{}: 0".format(ti))
                break
            groups += 1
        else:
            if rem:
                printf("Case #{}: 0".format(ti))
            else:
                res *= factorial(groups)
                printf("Case #{}: {}".format(ti, res % 1000000007))
