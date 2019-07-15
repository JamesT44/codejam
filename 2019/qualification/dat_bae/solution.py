def printf(*args, **kwargs): print(*args, **kwargs, flush=True)

queries = []
for i in range(5):
    rep = 2 ** i
    seed = "0" * rep + "1" * rep
    queries.append((seed * (1024 // len(seed) + 1)))

t = int(input())
for ti in range(1, t + 1):
    n, b, f = map(int, input().split())
    pairs = []
    for qr in queries:
        printf(qr[:n])
        response = input()
        pairs.append((qr[:n], response))

    qi, ri = 0, 0
    res = []
    while len(res) < b:
        if ri >= len(pairs[0][1]):
            res.append(qi)
            qi += 1
        elif all(q[qi] == r[ri] for q, r in pairs):
            qi += 1
            ri += 1
        else:
            res.append(qi)
            qi += 1
    printf(*res)
    assert(input() == "1")