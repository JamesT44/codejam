# import sys
# sys.stdin = open("large.in", "r")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    counts = [(int(x), chr(i + ord("A"))) for i, x in enumerate(input().split())]
    counts = sorted(counts)
    solution = []
    diff = counts[-1][0] - counts[-2][0]
    if diff:
        solution += [counts[-1][1]] * diff
    for i, party in counts[:-2]:
        solution += [party] * i
    solution += [counts[-2][1] + counts[-1][1]] * counts[-2][0]
    printf("Case #{}: {}".format(ti, " ".join(solution)))
