from collections import Counter
import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    s = Counter(input())
    res = [s.get("Z", 0),
           s.get("O", 0) - s.get("Z", 0) - s.get("W", 0) - s.get("U", 0),
           s.get("W", 0),
           s.get("H", 0) - s.get("G", 0),
           s.get("U", 0),
           s.get("F", 0) - s.get("U", 0),
           s.get("X", 0),
           s.get("S", 0) - s.get("X", 0),
           s.get("G", 0),
           s.get("I", 0) - s.get("G", 0) - s.get("X", 0) - s.get("F", 0) + s.get("U", 0)]
    printf("Case #{}: {}".format(ti, "".join(str(i) * res[i] for i in range(10))))
