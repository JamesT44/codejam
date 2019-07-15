import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    r, c = map(int, input().split())
    grid = [list(input()) for _ in range(r)]
    res = 0
    for x in range(r):
        for y in range(c):
            cell = grid[x][y]
            if cell == "^":
                if not any(grid[x2][y] != "." for x2 in range(x)):
                    res += 1
            elif cell == ">":
                if not any(grid[x][y2] != "." for y2 in range(y + 1, c)):
                    res += 1
            elif cell == "v":
                if not any(grid[x2][y] != "." for x2 in range(x + 1, r)):
                    res += 1
            elif cell == "<":
                if not any(grid[x][y2] != "." for y2 in range(y)):
                    res += 1
            if cell != "." and not (any(grid[x2][y] != "." and x != x2 for x2 in range(r)) or any(grid[x][y2] != "." and y != y2 for y2 in range(c))):
                break
        else:
            continue
        break
    else:
        printf("Case #{}: {}".format(ti, res))
        continue
    printf("Case #{}: IMPOSSIBLE".format(ti))