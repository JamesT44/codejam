from math import floor, ceil
import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, p = [int(x) for x in input().split(" ")]
    needed = [int(x) for x in input().split(" ")]
    packs = []
    count = 0
    for i in range(n):
        low, high = 9 * needed[i], 11 * needed[i]
        sizes = []
        for x in input().split(" "):
            z = int(x) * 10
            sizes.append(((z + high - 1) // high, z // low))
        packs.append(sorted(sizes))
    while all(packs):
        max_min = max(ingredient[0][0] for ingredient in packs)
        for ingredient in packs:
            if ingredient[0][1] < max_min:
                ingredient.pop(0)
                break
        else:
            for ingredient in packs:
                ingredient.pop(0)
            count += 1
    printf("Case #{}: {}".format(ti, count))
