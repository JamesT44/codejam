import sys

filename = "A-small-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    x = int(input())
    pos = None
    for i in range(4):
        if i + 1 == x:
            pos = set(map(int, input().split()))
        else:
            input()

    x = int(input())
    for i in range(4):
        if i + 1 == x:
            pos = set(map(int, input().split())).intersection(pos)
        else:
            input()

    if len(pos) == 1:
        printf("Case #{}: {}".format(ti, pos.pop()))
    elif len(pos) > 1:
        printf("Case #{}: Bad magician!".format(ti))
    else:
        printf("Case #{}: Volunteer cheated!".format(ti))