import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    done = False
    n = [int(x) for x in input()]
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            s = i
            n[i] -= 1
            for j in range(i + 1, len(n)):
                n[j] = 9
            break
    else:
        done = True
    if not done:
        for i in range(s, 0 , -1):
            if n[i] < n[i - 1]:
                n[i] = 9
                n[i - 1] -= 1
            else:
                done = True
    out = 0
    while n:
        out *= 10
        out += n.pop(0)
    printf("Case #{}: {}".format(ti, out))
