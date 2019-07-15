import sys

filename = "C-small-practice-2"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, k = map(int, input().split())
    k += 1
    u = float(input())
    p = list(sorted(map(float, input().split()))) + [1.0]
    res = 0
    for i in range(len(p)):
        pc = p[:]
        uc = u
        j = i
        while uc > 1e-10:
            if j == len(p) - 1:
                j = i - 1
                pc[j] += uc
                uc = 0
            else:
                l = j - i + 1
                x = min((pc[j + 1] - pc[j]) * l, uc)
                uc -= x
                x /= l
                for q in range(i, j + 1):
                    pc[q] += x
                j += 1
        successes = [0.0 for _ in range(k)]
        successes[0] = 1.0
        for prob in pc:
            successes = [successes[0] * (1 - prob)] + [successes[q] * prob + successes[q + 1] * (1 - prob) for q in range(k - 1)]
        res = max(res, 1 - sum(successes))
        if j == i - 1:
            break
    printf("Case #{}: {}".format(ti, res))
