import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    r, c, n = map(int, input().split())
    if n <= (r * c + 1) // 2:
        printf("Case #{}: {}".format(ti, 0))
        continue
    if r > c:
        r, c = c, r
    rem = r * c - n
    if r == 1:
        printf("Case #{}: {}".format(ti, c - 1 - 2 * (rem)))
        continue
    if r % 2 and c % 2:
        removable = r * c // 2
        inner = (r - 2) * (c - 2) // 2
        counts = [[inner + 1, removable - inner - 4], [inner, removable - inner]]
        res = 99e9
        for x, y in counts:
            score = r * c * 2 - r - c
            res = min(res, score - rem * 4 + max(rem - x, 0) + max(rem - x - y, 0))
        printf("Case #{}: {}".format(ti, res))
    else:
        removable = (r * c + 1) // 2
        inner = ((r - 2) * (c - 2) + 1) // 2
        outer = removable - inner - 2
        printf("Case #{}: {}".format(ti, r * c * 2 - r - c - rem * 4 + max(rem - inner, 0) + max(rem - inner - outer, 0)))
