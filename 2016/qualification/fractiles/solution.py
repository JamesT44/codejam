import sys

filename = "D-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    k, c, s = map(int, input().split())
    if c * s < k:
        printf("Case #{}: IMPOSSIBLE".format(ti))
        continue
    tiles = []
    for i in range(1, k + 1, c):
        p = 1
        for j in range(c):
            p = (p - 1) * k + min(i + j, k)
        tiles.append(p)
    printf("Case #{}:".format(ti), *tiles if tiles else "IMPOSSIBLE")
