import sys

filename = "D-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
	input()
	printf("Case #{}: {}".format(ti, sum(i + 1 != x for i, x in enumerate(map(int, input().split())))))
