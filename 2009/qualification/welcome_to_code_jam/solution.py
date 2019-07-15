import sys


filename = "C-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


target = {'w': {0}, 'e': {1, 6, 14}, 'l': {2}, 'c': {11, 3}, 'o': {9, 4, 12}, 'm': {18, 5}, ' ': {10, 15, 7}, 't': {8},
          'd': {13}, 'j': {16}, 'a': {17}}
t = int(input())
for ti in range(1, t + 1):
    s = input()
    counts = [0 for c in range(20)]
    counts[0] = 1
    for c in s:
        if c in target:
            for i in target[c]:
                counts[i + 1] += counts[i]
    printf("Case #{}: {:04d}".format(ti, counts[-1] % 10000))
