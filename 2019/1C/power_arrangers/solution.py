def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t, f = map(int, input().split())
for ti in range(1, t + 1):
    full = set("ABCDE")
    res = []
    group = range(0, 595, 5)
    for target in (24, 6, 2, 1):
        counts = {c: set() for c in full}
        for i in group:
            printf(i + 1)
            x = input()
            counts[x].add(i + 1)
        group = None
        for c in full:
            if len(counts[c]) != target:
                res.append(c)
                group = counts[c]
                full.remove(c)
                break
    printf("".join(res) + set("ABCDE").difference(set(res)).pop())
    input()
