def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    evens, odds = [], []
    for i, num in enumerate([int(x) for x in input().split(" ")]):
        if i % 2:
            odds.append(num)
        else:
            evens.append(num)
    evens.sort()
    odds.sort()
    for i in range(n - 1):
        if (i % 2 and odds[i // 2] > evens[i // 2 + 1]) or (i % 2 == 0 and evens[i // 2] > odds[i // 2]):
            printf("Case #{}: {}".format(ti, i))
            break
    else:
        printf("Case #{}: OK".format(ti))
