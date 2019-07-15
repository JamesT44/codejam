def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    weights = [int(x) for x in input().split(" ")]
    prev = [-1 for _ in range(141)]
    prev[0] = 0
    res = 0
    for w in weights:
        h = res
        while prev[h] > 6 * w:
            h -= 1
        if h == res:
            res += 1
        for h2 in range(h, -1, -1):
            if prev[h2 + 1] == -1 or prev[h2 + 1] > prev[h2] + w:
                prev[h2 + 1] = prev[h2] + w

    printf("Case #{}: {}".format(ti, res))
