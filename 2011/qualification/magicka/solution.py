import sys
from collections import Counter, defaultdict

filename = "B-small-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
	c, *items = input().split()
	combine = {}
	for s in items[:int(c)]:
		combine[(s[0], s[1])] = s[2]
		combine[(s[1], s[0])] = s[2]
	d, *items = items[int(c):]
	oppose = defaultdict(set)
	for s in items[:int(d)]:
		oppose[s[0]].add(s[1])
		oppose[s[1]].add(s[0])

	res = []
	sr = Counter()
	first = True
	for ch in items[-1]:
		if not res:
			res.append(ch)
			sr[ch] += 1
		elif (res[-1], ch) in combine:
			sr[res[-1]] -= 1
			res[-1] = combine[(res[-1], ch)]
			while len(res) >= 2 and (res[-2], res[-1]) in combine:
				sr[res[-2]] -= 1
				res[-2] = combine[(res[-2], res[-1])]
				res.pop()
			sr[res[-1]] += 1
			if res[-1] in oppose and any(sr[x] > 0 for x in oppose[res[-1]]):
				res = []
				sr = Counter()
		elif ch in oppose and any(sr[x] > 0 for x in oppose[ch]):
			res = []
			sr = Counter()
		else:
			res.append(ch)
			sr[ch] += 1

	printf("Case #{}: [{}]".format(ti, ", ".join(res)))
