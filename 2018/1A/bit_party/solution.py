def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    r, b, c = [int(x) for x in input().split(" ")]
    cashiers = []
    maxtime = 0
    for _ in range(c):
        m, s, p = [int(x) for x in input().split(" ")]
        time = m * s + p
        maxtime = max(maxtime, time)
        cashiers.append((m, s, p))
    tlow, thigh, tcheck = 0, maxtime, maxtime // 2
    while tlow != thigh:
        caps = []
        for m, s, p in cashiers:
            caps.append(max(0, min(m, (tcheck - p) // s)))
        caps.sort(reverse=True)
        if sum(caps[:r]) < b:
            tlow = tcheck + 1
        else:
            thigh = tcheck
        tcheck = (tlow + thigh) // 2

    printf("Case #{}: {}".format(ti, tcheck))
