from random import shuffle
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 100

print(tc)
for ti in range(tc):
    n = 10000
    print(n)
    p = list("ES" * 9999)
    shuffle(p)
    print("".join(p))
