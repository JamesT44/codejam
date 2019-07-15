import sys

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
	h, w = map(int, input().split())
	mapping = [list(map(int, input().split())) for _ in range(h)]
	res = [["" for _ in range(w)] for _ in range(h)]
	basin = ord("a")
	for ia in range(h):
		for ja in range(w):
			i, j = ia, ja
			if res[i][j]:
				continue
			group = [(i, j)]
			while not res[i][j]:
				best = (mapping[i][j], -1, -1)
				for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
					ni, nj = i + di, j + dj
					if ni == -1 or ni == h or nj == -1 or nj == w:
						continue
					if best[0] > mapping[ni][nj]:
						best = (mapping[ni][nj], ni, nj)
				if best[1] == -1:
					res[i][j] = chr(basin)
					basin += 1
				else:
					group.append(best[1:])
					i, j = best[1:]
			c = res[i][j]
			for i, j in group:
				res[i][j] = c
	printf("Case #{}:".format(ti))
	for row in res:
		printf(*row)
