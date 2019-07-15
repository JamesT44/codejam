from random import randint
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 100

print(tc)
for ti in range(tc):
    print(randint(1, 10**100))