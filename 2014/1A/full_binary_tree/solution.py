import sys
from functools import lru_cache

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")
sys.setrecursionlimit(5000)


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


@lru_cache(maxsize=None)
def solve(curr, parent):
    ra, rb = 0, 0
    for child in adj[curr]:
        if child != parent:
            x = solve(child, curr)
            if x > ra:
                ra, rb = x, ra
            elif x > rb:
                rb = x
    if ra and rb:
        return ra + rb + 1
    return 1


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    adj = [set() for i in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u - 1].add(v - 1)
        adj[v - 1].add(u - 1)
    res = n
    for root in range(n):
        res = min(res, n - solve(root, -1))
        if res == 0:
            break
    solve.cache_clear()
    printf("Case #{}: {}".format(ti, res))
