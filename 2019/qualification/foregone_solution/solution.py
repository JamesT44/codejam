def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n = input()
    b = int("".join(["1" if x == "4" else "0" for x in n]))
    printf("Case #{}: {} {}".format(ti, n.replace("4", "3"), b))
