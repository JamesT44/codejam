from math import gcd

def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, l = map(int, input().split())
    c = list(map(int, input().split()))
    start = 0
    while c[0] == c[1]:
        start += 1
        c.pop(0)
    g = gcd(c[0], c[1])
    p = [c[0] // g, g]
    for x in c[1:]:
        p.append(x // p[-1])
    for _ in range(start // 2):
        p = p[:2] + p
    if start % 2:
        p = [p[1]] + p

    key = {x: chr(i + ord("A")) for i, x in enumerate(sorted(set(p)))}
    printf("Case #{}: {}".format(ti, "".join(key[x] for x in p)))
