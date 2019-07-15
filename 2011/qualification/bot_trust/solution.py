import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
	_, *inp = input().split()
	seq = []
	sep = [[], []]
	for r, p in zip(inp[::2], inp[1::2]):
		robot = int(r == "O")
		p = int(p)
		seq.append((robot, p))
		sep[robot].append(p)

	pos = [1, 1]
	res = 0
	for r, p in seq:
		dt = abs(p - pos[r]) + 1
		res += dt
		pos[r] = p
		sep[r].pop(0)
		x = 1 - r
		if sep[x]:
			t = sep[x][0]
			if t > pos[x]:
				pos[x] = min(pos[x] + dt, t)
			else:
				pos[x] = max(pos[x] - dt, t)
	printf("Case #{}: {}".format(ti, res))
