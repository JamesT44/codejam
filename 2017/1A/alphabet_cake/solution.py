import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    r, c = [int(x) for x in input().split()]
    grid = []
    for _ in range(r):
        grid.append(list(input()))
    for x in range(1, c):
        for y in range(r):
            if grid[y][x] == "?":
                grid[y][x] = grid[y][x - 1]
    for x in range(c - 2, -1, -1):
        for y in range(r):
            if grid[y][x] == "?":
                grid[y][x] = grid[y][x + 1]
    for y in range(1, r):
        for x in range(c):
            if grid[y][x] == "?":
                grid[y][x] = grid[y - 1][x]
    for y in range(r - 2, -1, -1):
        for x in range(c):
            if grid[y][x] == "?":
                grid[y][x] = grid[y + 1][x]
    printf("Case #{}:".format(ti))
    for row in grid:
        printf("".join(row))
