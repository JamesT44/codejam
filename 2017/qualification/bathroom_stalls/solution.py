from collections import defaultdict
import sys

filename = "C-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, k = [int(x) for x in input().split(" ")]
    s = {n}
    c = defaultdict(int)
    c[n] = 1
    p = 0
    while True:
        x = max(s)
        xa = x // 2
        xb = (x - 1) // 2
        p += c[x]
        if p >= k:
            printf("Case #{}: {} {}".format(ti, xa, xb))
            break
        else:
            s.remove(x)
            s.add(xa)
            s.add(xb)
            c[xa] += c[x]
            c[xb] += c[x]
