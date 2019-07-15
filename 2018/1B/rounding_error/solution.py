from bisect import bisect_left
import sys

sys.stdin = open("large.in")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, l = map(int, input().split())
    counts = list(map(int, input().split()))
    ccounts = sorted(counts)
    rem = n - sum(counts)
    rs = [i for i in range(n) if int(0.5 + i * 100 / n) > i * 100 / n]
    if not 100 % n:
        printf("Case #{}: {}".format(ti, 100))
        continue
    m = rs[-1]
    needed = []
    for i, count in enumerate(counts):
        if count > m:
            needed.append((rem + 1, i))
        else:
            x = rs[bisect_left(rs, count)]
            if count - x <= rs[0]:
                needed.append((x - count, i))
    needed.sort()
    for x, i in needed:
        if x <= rem:
            rem -= x
            counts[i] += x
        if not rem:
            break
    m = rs[0]
    counts = counts + [m for _ in range(rem // m)] + [rem % m]
    printf("Case #{}: {}".format(ti, sum(int(0.5 + count * 100 / n) for count in counts)))
