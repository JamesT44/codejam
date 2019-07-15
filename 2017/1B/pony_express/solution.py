import sys

filename = "C-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, q = [int(x) for x in input().split(" ")]
    horses = [[int(x) for x in input().split(" ")] for _ in range(n)]
    dists = [[int(x) for x in input().split(" ")] for _ in range(n)]
    times = [[-1 for _ in range(n)] for __ in range(n)]
    journeys = [[int(x) - 1 for x in input().split(" ")] for _ in range(q)]

    for k in range(n):
        for i in range(n):
            if k == i:
                continue
            for j in range(n):
                if k == j or i == j:
                    continue
                first, second = dists[i][k], dists[k][j]
                if first != -1 and second != -1:
                    if dists[i][j] == -1:
                        dists[i][j] = first + second
                    else:
                        dists[i][j] = min(first + second, dists[i][j])

    for i in range(n):
        for j in range(n):
            dist = dists[i][j]
            if -1 < dist <= horses[i][0]:
                times[i][j] = dist / horses[i][1]

    for k in range(n):
        for i in range(n):
            if k == i:
                continue
            for j in range(n):
                if k == j or i == j:
                    continue
                first, second = times[i][k], times[k][j]
                if first != -1 and second != -1:
                    if times[i][j] == -1:
                        times[i][j] = first + second
                    else:
                        times[i][j] = min(first + second, times[i][j])

    out = " ".join("{:.7f}".format(times[i][j]) for i, j in journeys)
    printf("Case #{}: {}".format(ti, out))
