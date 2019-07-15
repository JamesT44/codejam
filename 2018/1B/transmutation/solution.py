import sys
from collections import defaultdict


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    m = int(input())
    recipesm = [defaultdict(int) for _ in range(m)]
    for i in range(m):
        for x in map(int, input().split()):
            recipesm[i][x - 1] = 1

    stock = list(map(int, input().split()))

    l, h = 0, sum(stock)
    while l != h:
        m = (l + h) // 2 + 1
        cstock = {i: n for i, n in enumerate(stock)}
        cstock[0] -= m
        recipes = [x.copy() for x in recipesm]
        while True:
            fail = False
            for i, n in cstock.items():
                if n <= 0:
                    if i in recipes[i].keys():
                        h = m - 1
                        fail = True
                    else:
                        cstock.pop(i)
                        for r, k in recipes[i].items():
                            if r not in cstock:
                                fail = True
                                break
                            cstock[r] += k * n
                        else:
                            while True:
                                for j, recipe in enumerate(recipes):
                                    if recipe[i]:
                                        q = recipes[j].pop(i)
                                        for r, k in recipes[i].items():
                                            recipes[j][r] += k * q
                                        break
                                else:
                                    break
                    break
            else:
                l = m
                break
            if fail:
                break
    printf("Case #{}: {}".format(ti, l))
