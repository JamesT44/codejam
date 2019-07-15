import sys

filename = "B-large-practice"


sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    s = input()
    c = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            c += 1
    if s[-1] == "-":
        c += 1
    printf("Case #{}: {}".format(ti, c))
