import sys
from bisect import insort


filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")

def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    turn = int(input())
    na, nb = map(int, input().split())
    events = []
    for _ in range(na):
        start, end = input().split()
        start, end = list(map(int, start.split(":"))), list(map(int, end.split(":")))
        insort(events, (start[0] * 60 + start[1], end[0] * 60 + end[1], 0))
    for _ in range(nb):
        start, end = input().split()
        start, end = list(map(int, start.split(":"))), list(map(int, end.split(":")))
        insort(events, (start[0] * 60 + start[1], end[0] * 60 + end[1], 1))
    trains = [[], []]
    for start, end, direction in events:
        x = direction
        if trains[direction] and trains[direction][0][0] <= start:
            x = trains[direction].pop(0)[1]
        insort(trains[1 - direction], (end + turn, x))
    d = [x for _, x in trains[0] + trains[1]]
    s = sum(d)
    printf("Case #{}: {} {}".format(ti, len(d) - s, s))
