import sys
from functools import reduce

filename = "C-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)

mul_table = [[ 0,  0,  0,  0,  0 ],
             [ 0,  1,  2,  3,  4 ],
             [ 0,  2, -1,  4, -3 ],
             [ 0,  3, -4, -1,  2 ],
             [ 0,  4,  3, -2, -1 ]]
def times(a, b):
    return mul_table[abs(a)][abs(b)] * (1 if a * b > 0 else -1)

def exp(x, n):
    if n == 1:
        return x
    elif n % 2:
        return times(x, exp(times(x, x), (n - 1) // 2))
    else:
        return exp(times(x, x), n // 2)

t = int(input())
for ti in range(1, t + 1):
    l, x = map(int, input().split())
    s = [ord(c) - 103 for c in input()]
    tot = exp(reduce(times, s), x)
    if tot != -1:
        printf("Case #{}: NO".format(ti))
        continue
    x = min(x, 8)
    i, j = 1, 1
    for a in range(x):
        for b in range(l):
            if i != 2:
                i = times(i, s[b])
            elif j != 3:
                j = times(j, s[b])
            else:
                break
        else:
            continue
        break
    if i == 2 and j == 3:
        print("Case #{}: YES".format(ti))
    else:
        print("Case #{}: NO".format(ti))