import sys

filename = "C-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
	r, k, n = map(int, input().split())
	g = list(map(int, input().split()))
	cycle = []
	starts = []
	tot = 0
	i = 0
	while True:
		c = 0
		starts.append(i)
		while c <= k:
			c += g[i]
			i += 1
			i %= n
			if i == starts[-1]:
				break
		i -= 1
		i %= n
		if c > k:
			c -= g[i]
		cycle.append(c)
		if i in starts:
			idx = starts.index(i)
			res = sum(cycle[:idx])
			r -= idx
			cycle = cycle[idx:]
			printf("Case #{}: {}".format(ti, res + r // len(cycle) * sum(cycle) + sum(cycle[:r % len(cycle)])))
			break
