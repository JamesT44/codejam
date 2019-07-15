from random import randint, choice
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 100
p = 3
q = 10
print(tc)
for _ in range(tc):
    print(p, q)
    all = [(randint(0, q), randint(0, q), choice("NESW")) for _ in range(p)]
    for x in all:
        print(*x)
    for x in all:
        print(*x)
