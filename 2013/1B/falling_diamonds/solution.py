import sys
from math import factorial

filename = "B-largecode-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


def binom(n, r):
    p = 1.0

    for i in range(r):
        p = p * (n - i) / (i + 1)

    return p


t = int(input())
for ti in range(1, t + 1):
    n, x, y = map(int, input().split())
    layer = ((abs(x) + y) // 2) + 1
    reached = int(((1 + 8 * n) ** 0.5 + 1) // 4)
    if layer <= reached:
        printf("Case #{}: {:0.6f}".format(ti, 1.0))
    elif layer > reached + 1 or n == reached * (2 * reached - 1):
        printf("Case #{}: {:0.6f}".format(ti, 0.0))
    else:
        extra = n - reached * (2 * reached - 1)
        height = y + 1
        if 2 * layer - 2 + height <= extra:
            printf("Case #{}: {:0.6f}".format(ti, 1.0))
        elif extra < height or height == 2 * layer - 1:
            printf("Case #{}: {:0.6f}".format(ti, 0.0))
        else:
            res = 0
            for i in range(height, extra + 1):
                res += factorial(extra) // factorial(i) // factorial(extra - i)
            printf("Case #{}: {:0.6f}".format(ti, res / (2 ** extra)))

    # N, X, Y = n, x, y
    # k = 1
    #
    # while (k + 2) * (k + 3) // 2 <= N:
    #     k += 2
    #
    # assert k % 2 == 1
    # level = abs(X) + Y + 1
    # assert level % 2 == 1
    #
    # if level <= k:
    #     print("Case #{0}: 1.0".format(0))
    # elif level > k + 2:
    #     print("Case #{0}: 0.0".format(0))
    # else:
    #
    #     assert level == k + 2
    #     d = N - k * (k + 1) // 2
    #     h = k + 1
    #     assert d <= 2 * h
    #
    #     if Y == h:
    #         print("Case #{0}: 0.0".format(0))
    #     elif d > h and Y < d - h:
    #         print("Case #{0}: 1.0".format(0))
    #     else:
    #         prob = 0.0
    #
    #         for j in range(Y + 1, d + 1):
    #             prob += binom(d, j)
    #
    #         prob /= 2**d
    #         print("Case #{}: {}".format(0, prob))
