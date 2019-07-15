import sys
from functools import reduce

filename = "C-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
	n = int(input())
	candy = list(map(int, input().split()))
	printf("Case #{}: {}".format(ti, "NO" if reduce(lambda x, y: x ^ y, candy) else sum(candy) - min(candy)))
