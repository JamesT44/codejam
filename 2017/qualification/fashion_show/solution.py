from collections import defaultdict
import sys

filename = "D-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    score = 0
    n, m = [int(x) for x in input().split()]
    old_grid = [["." for _ in range(n)] for __ in range(n)]
    new_grid = [["." for _ in range(n)] for __ in range(n)]
    empty_rows = set(range(n))
    empty_cols = set(range(n))
    empty_sums = set(range(2 * n - 1))
    empty_diffs = set(range(1 - n, n))
    changes = {}
    for _ in range(m):
        model, r, c = input().split()
        r, c = int(r) - 1, int(c) - 1
        old_grid[r][c] = new_grid[r][c] = model
        if model in "xo":
            empty_rows.remove(r)
            empty_cols.remove(c)
        if model in "+o":
            empty_sums.remove(r + c)
            empty_diffs.remove(r - c)
        if model == "o":
            score += 2
        else:
            score += 1

    for r in empty_rows:
        c = empty_cols.pop()
        if new_grid[r][c] == "+":
            new_grid[r][c] = "o"
            changes[(r, c)] = "o"
        else:
            new_grid[r][c] = "x"
            changes[(r, c)] = "x"
        score += 1

    sum_ref, diff_ref = {i: [] for i in range(2 * n - 1)}, {i: [] for i in range(1 - n, n)}
    for r in range(n):
        for c in range(n):
            sum_ref[r + c].append((r, c))
            diff_ref[r - c].append((r, c))
    for i in sum_ref.keys():
        sum_ref[i].sort(key=lambda x: len(diff_ref[x[0] - x[1]]))
    for i in diff_ref.keys():
        diff_ref[i].sort(key=lambda x: len(sum_ref[x[0] + x[1]]))
    for s in sorted(range(2 * n - 1), key=lambda x: len(sum_ref[x])):
        if s in empty_sums:
            for r, c in reversed(sum_ref[s]):
                if r - c in empty_diffs:
                    if new_grid[r][c] == "x":
                        new_grid[r][c] = "o"
                        changes[(r, c)] = "o"
                    else:
                        new_grid[r][c] = "+"
                        changes[(r, c)] = "+"
                    score += 1
                    empty_sums.remove(s)
                    empty_diffs.remove(r - c)
                    break
    printf("Case #{}: {} {}".format(ti, score, len(changes)))
    for (r, c), model in changes.items():
        printf("{} {} {}".format(model, r + 1, c + 1))
