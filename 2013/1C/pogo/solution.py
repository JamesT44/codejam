import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    x, y = map(int, input().split())
    t = abs(x) + abs(y)
    n = 0
    tot = 0
    while tot < t or (tot + x + y) % 2:
        n += 1
        tot += n
    res = []
    for i in range(n, 0, -1):
        if abs(x) > abs(y):
            if x > 0:
                res.append("E")
                x -= i
            else:
                res.append("W")
                x += i
        else:
            if y > 0:
                res.append("N")
                y -= i
            else:
                res.append("S")
                y += i
    printf("Case #{}: {}".format(ti, "".join(res[::-1])))