import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    s = input()
    out = [s[0]]
    for c in s[1:]:
        if c >= out[0]:
            out.insert(0, c)
        else:
            out.append(c)
    printf("Case #{}: {}".format(ti, "".join(out)))
