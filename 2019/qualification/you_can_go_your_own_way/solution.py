def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    p = input()
    printf("Case #{}: {}".format(ti, "".join("E" if c == "S" else "S" for c in p)))
