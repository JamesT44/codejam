# import sys
#
# filename = "-small-practice"
# sys.stdin = open(filename + ".in", "r")
# sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


winner = {"R": "P", "P": "S", "S": "R"}
loser = {v: k for k, v in winner.items()}

t = int(input())
for ti in range(1, t + 1):
    a = int(input())
    c = set(input() for _ in range(a))
    optimal = []
    i = 0
    while c:
        start = set(x[i % len(x)] for x in c)
        if len(start) == 3 or i == 500:
            optimal = []
            break
        if len(start) == 1:
            optimal.append(winner[start.pop()])
            break
        r = loser[{"R", "P", "S"}.difference(start).pop()]
        optimal.append(r)
        c = {x for x in c if x[i % len(x)] == r}
        i += 1
    printf("Case #{}: {}".format(ti, "".join(optimal) if optimal else "IMPOSSIBLE"))
