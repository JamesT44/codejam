# import sys
# sys.stdin = open("large.in", "r")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    d, n = [int(x) for x in input().split(" ")]
    answer = 0.0
    for hi in range(n):
        start, speed = [int(x) for x in input().split(" ")]
        answer = max(answer, (d - start) / speed)
    printf("Case #{}: {:6f}".format(ti, d / answer))
