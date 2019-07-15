import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, c, m = [int(x) for x in input().split(" ")]
    tickets = [[int(x) - 1 for x in input().split(" ")] for _ in range(m)]
    seats = [0] * n
    custs = [0] * c
    for seat, cust in tickets:
        seats[seat] += 1
        custs[cust] += 1
    trains = max(custs + [seats[0]])
    tot = 0
    for i in range(n):
        tot += seats[i]
        trains = max(trains, (tot + i) // (i + 1))
    promos = 0
    for i in range(n):
        if seats[i] > trains:
            promos += seats[i] - trains
    printf("Case #{}: {} {}".format(ti, trains, promos))
