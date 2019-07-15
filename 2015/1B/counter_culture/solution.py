import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = input()
    ln, n = len(n), int(n)
    if n < 21:
        printf("Case #{}: {}".format(ti, n))
    else:
        res = 10
        c = 10
        lc = len(str(c))
        while lc < ln:
            lr = lc // 2
            res += 10 ** lr * (11 if lc % 2 else 2) - 1
            c *= 10
            lc += 1
        rmod = 10 ** ((ln + 1) // 2)
        if n != c:
            if not n % 10:
                n -= 1
                res += 1
            v = str(n // rmod)[::-1]
            if int(v) > 1:
                res += int(v) + 1
                c = int(v[::-1]) * rmod + 1
            res += n - c
        printf("Case #{}: {}".format(ti, res))
