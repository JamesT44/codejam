from random import shuffle

def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    r, c = map(int, input().split())
    if tuple(sorted((r, c))) in [(2, 2), (2, 3), (2, 4), (3, 3)]:
        printf("Case #{}: IMPOSSIBLE".format(ti))
    else:
        printf("Case #{}: POSSIBLE".format(ti))
        while True:
            order = [(i, j) for i in range(r) for j in range(c)]
            shuffle(order)
            res = [order.pop()]
            while order:
                ux, uy = res[-1]
                for i, (vx, vy) in enumerate(order):
                    if ux != vx and uy != vy and ux + uy != vx + vy and ux - uy != vx - vy:
                        res.append((vx, vy))
                        order.pop(i)
                        break
                else:
                    break
            else:
                break
        for x, y in res:
            printf(x + 1, y + 1)
