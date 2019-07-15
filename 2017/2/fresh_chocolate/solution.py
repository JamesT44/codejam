import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, p = [int(x) for x in input().split(" ")]
    groups = [int(x) for x in input().split(" ")]
    gd = {x: 0 for x in range(p)}
    for g in groups:
        gd[g % p] += 1
    fresh = 0
    if p == 2:
        fresh = gd[0] + gd[1] - (gd[1] // 2)
    elif p == 3:
        fresh = gd[0] + min(gd[1], gd[2]) + ((abs(gd[1] - gd[2]) + 2) // 3)
    elif p == 4:
        fresh = gd[0] + min(gd[1], gd[3]) + (gd[2] // 2) + (gd[2] % 2) + ((abs(gd[1] - gd[3]) + 3 - (2 * (gd[2] % 2))) // 4)
    printf("Case #{}: {}".format(ti, fresh))
