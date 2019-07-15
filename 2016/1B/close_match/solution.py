import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


def check(a, b):
    for i in range(len(a)):
        if a[i] == b[i] != "?":
            continue
        if "?" != a[i] != b[i] != "?":
            swap = False
            if a[i] < b[i]:
                a, b = b, a
                swap = True
            a, b = int("".join(map(str, a)).replace("?", "0")), int("".join(map(str, b)).replace("?", "9"))
            if swap:
                a, b = b, a
            return abs(a - b), a, b
        if a[i] == b[i] == "?":
            a[i] = 0
            b[i] = 1
            res = check(a[:], b[:])
            a[i] = 1
            b[i] = 0
            res = min(res, check(a[:], b[:]))
            a[i] = 0
            b[i] = 0
            return min(res, check(a, b))
        swap = False
        if a[i] == "?":
            a, b = b, a
            swap = True
        res = (1e100, 1e100, 1e100)
        if a[i] != 9:
            b[i] = a[i] + 1
            res = min(res, check(a[:], b[:]))
        if a[i] != 0:
            b[i] = a[i] - 1
            res = min(res, check(a[:], b[:]))
        b[i] = a[i]
        res = min(res, check(a[:], b[:]))
        if swap:
            return res[0], res[2], res[1]
        return res
    a, b = int("".join(map(str, a))), int("".join(map(str, b)))
    return abs(a - b), a, b


t = int(input())
for ti in range(1, t + 1):
    a, b = input().split()
    l = str(len(a))
    a, b = list(c if c == "?" else int(c) for c in a), list(c if c == "?" else int(c) for c in b)
    res = check(a, b)
    printf(("Case #{}: {:0" + l + "d} {:0" + l + "d}").format(ti, res[1], res[2]))
