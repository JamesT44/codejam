import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    grid = [list(input()) for _ in range(4)]
    diagonals = [[grid[i][i] for i in range(4)], [grid[3 - i][i] for i in range(4)]]
    input()
    xs, os = set("XT"), set("OT")
    if any(set(row) <= xs for row in grid + diagonals) or any(set(col) <= xs for col in zip(*grid)):
        printf("Case #{}: X won".format(ti))
    elif any(set(row) <= os for row in grid + diagonals) or any(set(col) <= os for col in zip(*grid)):
        printf("Case #{}: O won".format(ti))
    elif any("." in row for row in grid):
        printf("Case #{}: Game has not completed".format(ti))
    else:
        printf("Case #{}: Draw".format(ti))
