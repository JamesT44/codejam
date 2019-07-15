from random import randint
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 100
n = 100
print(tc)
for t in range(tc):
    print(n)
    print(*[randint(1, 1000) for _ in range(n)])
