from random import randint
import numpy as np
import sys

filename = "large.in"
sys.stdout = open(filename, "w")
tc = 50

print(tc)
for ti in range(tc):
    n = randint(2, 26)
    print(n)
    print(" ".join(str(x) for x in np.random.multinomial(1000, np.ones(n) / n, size=1)[0]))
