import sys
from bisect import insort, bisect_left, bisect_right

filename = "C-large-practice-2"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


res = [9, 484]

evens = [(0, 0), (11, 2)]
for l in range(2, 52, 2):
	nevens = []
	x = 10 ** (l - 1)
	y = x * 100
	for p, used in evens:
		if x <= p:
			insort(res, p * p)
		if used > 7:
			continue
		nevens.append((p * 10, used))
		nevens.append((p * 10 + 1 + y, used + 2))
		if used <= 1:
			nevens.append((p * 10 + 2 + y + y, used + 8))
	evens = nevens

odds = [(0, 0), (1, 1), (2, 4)]
for l in range(1, 52, 2):
	nodds = []
	x = 10 ** (l - 1)
	y = x * 100
	for p, used in odds:
		if x <= p:
			insort(res, p * p)
		if used > 7:
			continue
		nodds.append((p * 10, used))
		nodds.append((p * 10 + 1 + y, used + 2))
		if used <= 1:
			nodds.append((p * 10 + 2 + y + y, used + 8))
	odds = nodds

res = [x for x in res if x <= 1e100]

t = int(input())
for ti in range(1, t + 1):
	a, b = map(int, input().split())
	printf("Case #{}: {}".format(ti, bisect_right(res, b) - bisect_left(res, a)))
