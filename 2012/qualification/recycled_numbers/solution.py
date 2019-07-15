import sys

filename = "C-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    print(ti, file=sys.stderr)
    a, b = map(int, input().split())
    p = 10 ** (len(str(a)) - 1)
    res = 0
    for n in range(a, b):
        m = n
        while True:
            m = m // 10 + ((m % 10) * p)
            if m == n:
                break
            if n < m <= b:
                res += 1
    printf("Case #{}: {}".format(ti, res))
