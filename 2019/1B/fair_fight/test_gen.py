from random import randint
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 100
n = 3
print(tc)
for t in range(tc):
    n = 1000 #10 ** 5 if m < 8 else 1000
    k = randint(1, 10 ** 5)
    print(n, k)
    print(*[randint(0, 10 ** 5) for _ in range(n)])
    print(*[randint(0, 10 ** 5) for _ in range(n)])
