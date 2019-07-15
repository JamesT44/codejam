import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    s, k = input().split()
    s = list(s)
    k = int(k)
    count = 0
    for i in range(len(s) - k + 1):
        if s[i] == "-":
            count += 1
            for j in range(i, i + k):
                if s[j] == "+":
                    s[j] = "-"
                else:
                    s[j] = "+"
    for i in range(len(s) - k + 1, len(s)):
        if s[i] != "+":
            printf("Case #{}: IMPOSSIBLE".format(ti))
            break
    else:
        printf("Case #{}: {}".format(ti, count))
