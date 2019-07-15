import sys

filename = "C-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    r, c, m = map(int, input().split())
    e = r * c - m
    printf("Case #{}:".format(ti))
    if r == 1:
        printf(("*" * m) + ((c - m - 1) * ".") + "c")
    elif c == 1:
        for ch in ("*" * m) + ((r - m - 1) * ".") + "c":
            printf(ch)
    elif e == 1:
        for _ in range(r - 1):
            printf("*" * c)
        printf(("*" * (c - 1)) + "c")
    elif e <= 3:
        printf("Impossible")
    elif (r == 2 or c == 2) and m % 2:
        printf("Impossible")
    elif r == 2:
        printf(("*" * (m // 2)) + ("." * (e // 2)))
        printf(("*" * (m // 2)) + ("." * (e // 2 - 1)) + "c")
    elif c == 2:
        for _ in range(m // 2):
            printf("**")
        for _ in range(e // 2 - 1):
            printf("..")
        printf(".c")
    elif e >= 3 * c:
        while m:
            if m >= c:
                printf("*" * c)
                m -= c
                r -= 1
            elif m <= c - 2:
                printf(("*" * m) + ("." * (c - m)))
                r -= 1
                break
            else:
                printf(("*" * (c - 2)) + "..")
                printf("*" + ("." * (c - 1)))
                r -= 2
                break
        for _ in range(r - 1):
            printf("." * c)
        printf(("." * (c - 1)) + "c")
    elif 9 <= e < 3 * c:
        for _ in range(r - 3):
            printf("*" * c)
        m = 3 * c - e
        counts = [(m + 2) // 3, (m + 1) // 3, m // 3]
        if m % 3 == 2:
            counts[0] += 1
            counts[1] -= 1
        printf(("*" * counts[0]) + ("." * (c - counts[0])))
        printf(("*" * counts[1]) + ("." * (c - counts[1])))
        printf(("*" * counts[2]) + ("." * (c - counts[2] - 1)) + "c")
    elif e in (5, 7):
        printf("Impossible")
    elif e == 4:
        for _ in range(r - 2):
            printf("*" * c)
        printf(("*" * (c - 2)) + "..")
        printf(("*" * (c - 2)) + ".c")
    elif e == 6:
        for _ in range(r - 2):
            printf("*" * c)
        printf(("*" * (c - 3)) + "...")
        printf(("*" * (c - 3)) + "..c")
    elif e == 8:
        for _ in range(r - 3):
            printf("*" * c)
        printf(("*" * (c - 2)) + "..")
        printf(("*" * (c - 3)) + "...")
        printf(("*" * (c - 3)) + "..c")
