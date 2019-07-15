import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    counts = {}
    for _ in range(2 * n - 1):
        for c in input().split():
            x = int(c)
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
    out = []
    for k, v in counts.items():
        if v % 2:
            out.append(k)
    printf("Case #{}: {}".format(ti, " ".join(str(x) for x in sorted(out))))
