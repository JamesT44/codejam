import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    e, r, n = map(int, input().split())
    v = list(map(int, input().split()))
    ni = [-1] * n
    stack = []
    for i, x in enumerate(v):
        while stack and stack[-1][0] < x:
            ni[stack.pop()[1]] = i
        stack.append((x, i))
    res = 0
    energy = e
    for i, x in enumerate(v):
        if ni[i] == -1:
            res += x * energy
            energy = 0
        else:
            s = max(min(energy + (ni[i] - i) * r - e, energy), 0)
            energy -= s
            res += s * x
        energy = min(energy + r, e)
    printf("Case #{}: {}".format(ti, res))