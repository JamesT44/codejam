import sys

filename = "C-large-practice"


sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
n, jj = [int(x) for x in input().split(" ")]

done = False
printf("Case #1:")
for i in range(n - 10):
    for j in range(n - 10 - i):
        for k in range(n - 10 - i - j):
            l = n - 10 - i - j - k
            print("11" + ("0" * i) + "11" + ("0" * j) + "11" + ("0" * k) + "11" + ("0" * l) + "11 3 2 5 2 7 2 3 2 11")
            jj -= 1
            if not jj:
                done = True
                break
        if done:
            break
    if done:
        break
