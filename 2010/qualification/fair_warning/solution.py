import sys
from math import gcd

filename = "B-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
	_, *nums = map(int, input().split())
	m = abs(nums[0] - nums[1])
	for a, b in zip(nums[1: - 1], nums[2:]):
		m = gcd(m, a - b)
	printf("Case #{}: {}".format(ti, nums[0] % m))
