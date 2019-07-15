import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    b, m = map(int, input().split())
    if m > 2 ** (b - 2):
        printf("Case #{}: IMPOSSIBLE".format(ti, 0))
    else:
        printf("Case #{}: POSSIBLE".format(ti, 0))
        if m == 2 ** (b - 2):
            printf("0" + ("1" * (b - 1)))
        else:
            printf(("0{:0" + str(b - 2) + "b}0").format(m))
        for i in range(2, b + 1):
            printf(("0" * i) + ("1" * (b - i)))
