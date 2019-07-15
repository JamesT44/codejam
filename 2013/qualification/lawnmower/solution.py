import sys
from collections import defaultdict

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    groups = defaultdict(set)
    for i in range(n):
        for j in range(m):
            groups[grid[i][j]].add((i, j))
    curr = set()
    for layer in list(sorted(groups.keys()))[:-1]:
        curr.update(groups[layer])
        rem = curr.copy()
        while rem:
            x, y = rem.pop()
            row, col = set((x, i) for i in range(m)), set((i, y) for i in range(n))
            if not(row <= curr or col <= curr):
                printf("Case #{}: NO".format(ti))
                break
            if row <= curr:
                rem -= row
            if col <= curr:
                rem -= col
        else:
            continue
        break
    else:
        printf("Case #{}: YES".format(ti))
