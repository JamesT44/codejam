from math import sqrt, acos, cos, sin


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    a = float(input())
    theta = acos((2 * a + sqrt(24 - 8 * a * a)) / 6)
    s, c = sin(theta), cos(theta)
    p, q, r = (1 + c) / 4, (1 - c) / 4, sqrt(2) * s / 4
    printf("Case #{}:".format(ti))
    for row in [[p, r, q], [-r, p - q, r], [q, -r, p]]:
        printf("{:0.10f} {:0.10f} {:0.10f}".format(*row))
