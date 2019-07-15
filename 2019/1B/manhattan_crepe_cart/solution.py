from bisect import insort


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    p, q = map(int, input().split())
    q += 1
    xs, ys = [], []
    for _ in range(p):
        x, y, d = input().split()
        if d in "N":
            insort(ys, (int(y) + 1, False))
        elif d == "S":
            insort(ys, (int(y), True))
        elif d == "E":
            insort(xs, (int(x) + 1, False))
        elif d == "W":
            insort(xs, (int(x), True))
    rx, ry = 0, 0
    m, c = 0, 0
    for i in range(len(xs)):
        x, out = xs[i]
        if out:
            c -= 1
        else:
            c += 1
        if c > m and not (i < len(xs) - 1 and xs[i + 1][0] == x):
            rx = x
            m = c
    m, c = 0, 0
    for i in range(len(ys)):
        y, out = ys[i]
        if out:
            c -= 1
        else:
            c += 1
        if c > m and not (i < len(ys) - 1 and ys[i + 1][0] == y):
            ry = y
            m = c
    printf("Case #{}: {} {}".format(ti, rx, ry))


    # p, q = map(int, input().split())
    # q += 1
    xs, ys = [0] * q, [0] * q
    for _ in range(p):
        x, y, d = input().split()
        if d in "N":
            for i in range(int(y) + 1, q):
                ys[i] += 1
        elif d == "S":
            for i in range(int(y)):
                ys[i] += 1
        elif d == "E":
            for i in range(int(x) + 1, q):
                xs[i] += 1
        elif d == "W":
            for i in range(int(x)):
                xs[i] += 1
    printf("2Case #{}: {} {}".format(ti, xs.index(max(xs)), ys.index(max(ys))))
