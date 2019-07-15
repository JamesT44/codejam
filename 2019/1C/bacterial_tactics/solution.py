import functools


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


@functools.lru_cache(maxsize=None)
def nim(grid):
    children = []
    for i in range(len(grid)):
        if "#" not in grid[i]:
            children.append((grid[:i], grid[i + 1:], False))
    grid = tuple(zip(*grid))
    for i in range(len(grid)):
        if "#" not in grid[i]:
            children.append((grid[:i], grid[i + 1:], True))
    if not children:
        return (0, 0)
    else:
        r, c = len(grid), len(grid[0])
        res = [0]
        for a, b, flip in children:
            an, _ = nim(a)
            bn, _ = nim(b)
            nn = an ^ bn
            if len(res) < nn + 1:
                res += [0 for _ in range(nn + 1 - len(res))]
            res[nn] += c if flip else r
        res.append(0)
        return (res.index(0), res[0])


t = int(input())
for ti in range(1, t + 1):
    r, c = map(int, input().split())
    grid = tuple(tuple(input()) for _ in range(r))
    printf("Case #{}: {}".format(ti, nim(grid)[0]))
