import sys

filename = "A-large-practice"


sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    if not n:
        printf("Case #{}: INSOMNIA".format(ti))
        continue
    digits = set([int(x) for x in str(n)])
    nn = n
    while len(digits) < 10:
        nn += n
        digits.update([int(x) for x in str(nn)])
    printf("Case #{}: {}".format(ti, nn))
