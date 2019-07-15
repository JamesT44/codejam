from random import randint
from string import ascii_uppercase
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 100

print(tc)
for ti in range(tc):
    print(100)
    counts = [1] + [0 for _ in range(98)] + [1]
    for _ in range(98):
        counts[randint(0, 99)] += 1
    print(" ".join(map(str, counts)))
