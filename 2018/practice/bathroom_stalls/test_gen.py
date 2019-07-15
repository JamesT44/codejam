from random import randint
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 100

print(tc)
for ti in range(tc):
    n = randint(1, 10 ** 18)
    k = randint(1, n)
    print(n, k)
