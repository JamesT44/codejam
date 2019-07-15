from math import pi
import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, k = [int(x) for x in input().split(" ")]
    pancakes = [[int(x) for x in input().split(" ")] for _ in range(n)]
    pancakes = list(sorted([[2 * pi * r * h, r * r * pi] for r, h in pancakes], key=lambda x: x[1], reverse=True))
    best = 0
    for pancake in pancakes[:n-k+1]:
        pool = list(filter(lambda x: x[1] <= pancake[1], pancakes))
        pool.remove(pancake)
        pool.sort(reverse=True)
        best = max(best, sum(pancake) + sum(x[0] for x in pool[:k - 1]))
    printf("Case #{}: {:.6f}".format(ti, best))
