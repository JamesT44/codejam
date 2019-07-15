def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    sold = set()
    counts = [0 for _ in range(n)]
    for _ in range(n):
        flavours = [int(x) for x in input().split(" ")][1:]
        for f in flavours:
            counts[f] += 1
        available = list(filter(lambda x: x not in sold, flavours))
        if not len(available):
            printf(-1)
            continue
        besta, bestc = available[0], counts[available[0]]
        for a in available[1:]:
            if counts[a] < bestc:
                besta, bestc = a, counts[a]
        printf(besta)
        sold.add(besta)
