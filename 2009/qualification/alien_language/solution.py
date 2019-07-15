import sys
import re

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


l, d, n = map(int, input().split())
words = [input() for _ in range(d)]

for ti in range(1, n + 1):
	pattern = re.compile(input().replace("(", "[").replace(")", "]"))
	printf("Case #{}: {}".format(ti, sum(1 if pattern.match(word) else 0 for word in words)))
