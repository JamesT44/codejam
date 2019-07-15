import sys
from itertools import product

filename = "C-large-practice"


sys.stdin = open(filename + ".in", "r")
# sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for ti in range(1, t + 1):
    r, c = [int(x) for x in input().split(" ")]
    grid = [list(input()) for _ in range(r)]
    shooters = []
    sc = set()
    lmirrors = set()
    rmirrors = set()
    walls = set()
    spaces = set()
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x in "-|":
                shooters.append([i, j, 3, set(), set()])
                sc.add((i, j))
            elif x == "/":
                lmirrors.add((i, j))
            elif x == "\\":
                rmirrors.add((i, j))
            elif x == "#":
                walls.add((i, j))
            else:
                spaces.add((i, j))
    for ind, shooter in enumerate(shooters):
        i, j = shooter[:2]
        for dir in directions:
            travelled = []
            failed = False
            d = dir
            loc = (i + d[0], j + d[1])
            while True:
                if loc in sc:
                    failed = True
                    break
                elif loc in lmirrors:
                    d = [-d[1], -d[0]]
                elif loc in rmirrors:
                    d = d[::-1]
                elif loc in spaces:
                    travelled.append(loc)
                else:
                    break
                loc = (loc[0] + d[0], loc[1] + d[1])
            if failed:
                if dir[0] and shooter[2] >= 2:
                    shooters[ind][2] -= 2
                elif dir[1] and shooter[2] % 2:
                    shooters[ind][2] -= 1
            else:
                if dir[0]:
                    shooters[ind][3].update(travelled)
                else:
                    shooters[ind][4].update(travelled)
    rshooters = []
    unvisited = set(spaces)
    rest = set()
    done = False
    for shooter in shooters:
        if not shooter[2]:
            printf("Case #{}: IMPOSSIBLE".format(ti))
            done = True
            break
        elif shooter[2] == 3:
            rshooters.append(shooter)
            rest.update(shooter[3], shooter[4])
        elif shooter[2] == 2:
            unvisited = unvisited.difference(shooter[3])
            grid[shooter[0]][shooter[1]] = "|"
        elif shooter[2] == 1:
            unvisited = unvisited.difference(shooter[4])
            grid[shooter[0]][shooter[1]] = "-"
    if done:
        continue
    if unvisited.difference(rest):
        printf("Case #{}: IMPOSSIBLE".format(ti))
        continue


    found = False
    for solution in product(range(2), repeat=len(rshooters)):
        visited = set()
        for s, shooter in zip(solution, rshooters):
            if s:
                visited.update(shooter[3])
            else:
                visited.update(shooter[4])
        if len(visited) >= len(unvisited):
            for s, shooter in zip(solution, rshooters):
                if s:
                    grid[shooter[0]][shooter[1]] = "|"
                else:
                    grid[shooter[0]][shooter[1]] = "-"
            printf("Case #{}: POSSIBLE".format(ti))
            for row in grid:
                printf("".join(row))
            break

    else:
        printf("Case #{}: IMPOSSIBLE".format(ti))
