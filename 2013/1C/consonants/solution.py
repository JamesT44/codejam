import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    l, n = input().split()
    n = int(n)
    length = len(l)
    res = 0
    groups = []
    prev = False
    for i, c in enumerate(l):
        if c in "aeiou":
            if prev:
                if groups[-1][1] < n:
                    groups.pop()
                prev = False
        else:
            if prev:
                groups[-1][1] += 1
            else:
                groups.append([i, 1])
                prev = True
    if groups and groups[-1][1] < n:
        groups.pop()
    if not groups:
        printf("Case #{}: {}".format(ti, 0))
    else:
        res = 0
        for i in range(length):
            if i > sum(groups[0]) - n:
                groups.pop(0)
                if not groups:
                    break
            res += length - max(groups[0][0], i) - n + 1
        printf("Case #{}: {}".format(ti, res))
