import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    base = []
    counts = []
    for c in input():
        if base and base[-1] == c:
            counts[-1][0] += 1
        else:
            base.append(c)
            counts.append([1])
    l = len(base)
    for d in range(n - 1):
        i = 0
        count = 0
        for c in input():
            if i < l and c == base[i]:
                count += 1
            elif count == 0 or i == l - 1 or c != base[i + 1]:
                break
            else:
                counts[i].append(count)
                i += 1
                count = 1
        else:
            if i != l - 1:
                for _ in range(n - d - 2):
                    input()
                break
            counts[i].append(count)
            continue
        for _ in range(n - d - 2):
            input()
        break
    else:
        res = 0
        for group in counts:
            if n % 2:
                x = (list(sorted(group))[n // 2])
            else:
                x = sum(list(sorted(group))[n // 2 - 1:n // 2 + 1]) // 2
            for g in group:
                res += abs(x - g)
        printf("Case #{}: {}".format(ti, res))
        continue

    printf("Case #{}: Fegla Won".format(ti))