from functools import reduce
from itertools import product
# import sys
# sys.stdin = open("large.in", "r")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, l = [int(x) for x in input().split(" ")]
    words = set()
    inds = [set() for _ in range(l)]
    for _ in range(n):
        word = input()
        words.add(word)
        for i, c in enumerate(word):
            inds[i].add(c)
    maxwords = reduce(lambda x, y: x * y, map(lambda x: len(x), inds))
    if len(words) == maxwords:
        printf("Case #{}: -".format(ti))
        continue
    for word in product(*inds):
        x = "".join(word)
        if x not in words:
            printf("Case #{}: {}".format(ti, x))
            break
