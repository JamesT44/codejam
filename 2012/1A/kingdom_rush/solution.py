import sys
from bisect import insort, bisect


filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    levels = [[], []]
    rev = []
    for i in range(n):
        a, b = map(int, input().split())
        insort(levels[0], (a, b, i))
        insort(levels[1], (b, i))
        rev.append(a)
    rem = set(range(n))
    res = 0
    stars = 0
    while levels[1]:
        if levels[1][0][0] <= stars:
            stars += 1
            res += 1
            b, i = levels[1].pop(0)
            if i in rem:
                levels[0].pop(bisect(levels[0], (rev[i], b, i)) - 1)
                stars += 1
                rem.remove(i)
        elif levels[0] and levels[0][0][0] <= stars:
            best, bidx = levels[0][0], 0
            for i, level in enumerate(levels[0]):
                if level[0] > stars:
                    break
                if level[1] > best[1]:
                    best, bidx = level, i
            _, _, i = levels[0].pop(bidx)
            rem.remove(i)
            stars += 1
            res += 1
        else:
            printf("Case #{}: Too Bad".format(ti))
            break
    else:
        printf("Case #{}: {}".format(ti, res))
