import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


def pair(x, y):
    if x == y:
        return x
    else:
        return 0


t = int(input())
for ti in range(1, t + 1):
    ac, aj = [int(x) for x in input().split(" ")]
    swaps = 0
    leftc, leftj = 720, 720
    acs = []
    for _ in range(ac):
        start, end = [int(x) for x in input().split(" ")]
        acs.append([start, end, 1])
        leftc -= end - start
    for _ in range(aj):
        start, end = [int(x) for x in input().split(" ")]
        acs.append([start, end, -1])
        leftj -= end - start
    acs.sort()
    intervals = []
    start, end = acs[-1][1], acs[0][0]
    intervals.append([pair(acs[0][2], acs[-1][2]), 1440 + end - start])
    for i in range(len(acs) - 1):
        intervals.append([pair(acs[i][2], acs[i + 1][2]), acs[i + 1][0] - acs[i][1]])
    intervals.sort()
    for person, duration in intervals:
        if person == 1:
            if duration <= leftc:
                leftc -= duration
            else:
                swaps += 2
        elif person == -1:
            if duration <= leftj:
                leftj -= duration
            else:
                swaps += 2
        else:
            swaps += 1

    printf("Case #{}: {}".format(ti, swaps))
