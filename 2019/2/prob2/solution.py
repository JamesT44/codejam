def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    vases = []
    cands = []
    while True:
        d = int(input())
        if d <= 60:
            printf((d - 1) % 15 + 1, (d - 1) // 15 + 1)
        elif d <= 80:
            printf(d - 60, 0)
            vases.append([len(list(map(int, input().split()[1:]))), len(vases)])
            if d == 80:
                a = list(sorted(vases))
                cands = [a[0][1], a[1][1]]
        elif d <= 94:
            x = min(v for v in vases if v[1] not in cands)[1]
            printf(x + 1, 1)
            vases[x][0] += 1
        elif d <= 96:
            printf(cands[d - 95] + 1, 0)
            cands.append(len(list(map(int, input().split()[1:]))))
            if d == 96:
                if cands[3] < cands[2]:
                    cands[0], cands[1] = cands[1], cands[0]
        elif d <= 99:
            printf(cands[1] + 1, 1)
        else:
            printf(cands[0] + 1, 100)
            break
