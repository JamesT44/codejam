from random import sample, randint
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 100

print(tc)
for ti in range(tc):
    print(10 ** 9, 1000)
    for start in sample(range(1, 10 ** 9), 1000):
        print(start, randint(1, 10000))
