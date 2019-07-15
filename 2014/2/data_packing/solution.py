import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, x = map(int, input().split())
    s = list(sorted(map(int, input().split())))
    res = 0
    while s:
        if s.pop() + (s[0] if s else x) <= x:
            s.pop(0)
        res += 1
    printf("Case #{}: {}".format(ti, res))