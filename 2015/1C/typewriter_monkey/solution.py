import sys
from functools import reduce
from collections import Counter

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    k, l, s = map(int, input().split())
    keyboard = input()
    kcounts = {c: n / k for c, n in Counter(keyboard).most_common()}
    target = input()

    overlap = 0
    for i in range(l - 1, 0, -1):
        if target[:i] == target[-i:]:
            overlap = i
            break
    maximum = (s - l) // (l - overlap) + 1 if set(target) <= set(keyboard) and s >= l else 0
    expected = (s - l + 1) * reduce(lambda x, y: x * y, (kcounts[c] for c in target)) if maximum else 0

    printf("Case #{}: {:7f}".format(ti, maximum - expected))