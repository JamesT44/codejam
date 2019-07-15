import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
	n, k = map(int, input().split())
	printf("Case #{}: {}".format(ti, "OFF" if (k + 1) % (2 ** n) else "ON"))
