def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    d, p = input().split(" ")
    d = int(d)
    if p.count("S") > d:
        printf("Case #{}: IMPOSSIBLE".format(ti))
        continue
    groups = [0]
    damage = -d
    hacks = 0
    for c in p:
        if c == "C":
            groups.append(0)
        else:
            groups[-1] += 1
            damage += 2 ** (len(groups) - 1)
    if damage <= 0:
        printf("Case #{}: 0".format(ti))
        continue
    for i in range(len(groups) - 1, -1, -1):
        if groups[i] * (2 ** (i - 1)) >= damage:
            hacks += (damage + (2 ** (i - 1)) - 1) // (2 ** (i - 1))
            break
        else:
            groups[i - 1] += groups[i]
            hacks += groups[i]
            damage -= groups[i] * (2 ** (i - 1))
    printf("Case #{}: {}".format(ti, hacks))
