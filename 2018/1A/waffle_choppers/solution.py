def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    r, c, h, v = [int(x) for x in input().split(" ")]
    grid = [list(input()) for _ in range(r)]
    chips = 0
    for row in grid:
        chips += row.count("@")
    if chips % ((h + 1) * (v + 1)):
        printf("Case #{}: IMPOSSIBLE".format(ti))
        continue
    if not chips:
        printf("Case #{}: POSSIBLE".format(ti))
        continue

    cumh = [0]
    cumv = [0]
    for row in grid:
        cumh.append(cumh[-1] + row.count("@"))
    for i in range(c):
        cumv.append(cumv[-1] + [row[i] for row in grid].count("@"))
    failed = False
    hcuts, vcuts = [0], [0]
    for x in range(chips//(h+1), chips - 1, chips//(h+1)):
        if x not in cumh:
            failed = True
            break
        else:
            hcuts.append(cumh.index(x))
    for x in range(chips//(v+1), chips - 1, chips//(v+1)):
        if x not in cumv:
            failed = True
            break
        else:
            vcuts.append(cumv.index(x))
    if failed:
        printf("Case #{}: IMPOSSIBLE".format(ti))
        continue
    hcuts.append(r)
    vcuts.append(c)
    target = chips // ((h + 1) * (v + 1))
    groups = []
    for i in range(h + 1):
        groups.append(grid[hcuts[i]:hcuts[i+1]])
    for group in groups:
        for i in range(v + 1):
            subg = [row[vcuts[i]:vcuts[i+1]] for row in group]
            tcount = 0
            for row in subg:
                tcount += row.count("@")
            if tcount != target:
                failed = True
                break
        if failed:
            break
    if failed:
        printf("Case #{}: IMPOSSIBLE".format(ti))
    else:
        printf("Case #{}: POSSIBLE".format(ti))
