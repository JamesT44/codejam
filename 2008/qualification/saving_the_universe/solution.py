import sys


filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")

def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    s = int(input())
    for _ in range(s):
        input()
    q = int(input())
    res = 0
    group = set()
    for _ in range(q):
        x = input()
        group.add(x)
        if len(group) == s:
            res += 1
            group = {x}
    printf("Case #{}: {}".format(ti, res))
