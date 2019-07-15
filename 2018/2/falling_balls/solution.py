import sys

# sys.stdin = open("large.in")


def printf(output):
    sys.stdout.write(output + "\n")
    sys.stdout.flush()


t = int(sys.stdin.readline())
for ti in range(1, t + 1):
    c = int(sys.stdin.readline())
    balls = [int(x) for x in sys.stdin.readline().split(" ")]
    if balls[0] == 0 or balls[-1] == 0:
        printf("Case #{}: {}".format(ti, "IMPOSSIBLE"))
        continue
    cols = [[] for _ in range(c)]
    col_i = 0
    locs = []
    max_diff = 0
    for ball in range(c):
        while len(cols[col_i]) == balls[col_i]:
            col_i += 1
        cols[col_i].append(ball)
        locs.append(col_i)
        max_diff = max(max_diff, abs(col_i - ball))
    printf("Case #{}: {}".format(ti, max_diff + 1))
    grid = [["." for _ in range(c)] for __ in range(max_diff + 1)]
    assert(0 in cols[0])
    assert(c - 1 in cols[c - 1])
    for i, loc in enumerate(locs):
        if i == loc:
            continue
        if i < loc:
            for r in range(loc - i):
                grid[r][i + r] = "\\"
        else:
            for r in range(i - loc):
                grid[r][i - r] = "/"
    for row in grid:
        printf("".join(row))
