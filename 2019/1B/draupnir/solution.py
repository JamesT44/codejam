def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t, w = map(int, input().split())
for ti in range(1, t + 1):
    printf(224)
    x = int(input())
    printf(56)
    y = int(input())
    res = [x >> 56, (x >> 44) & 127, (x >> 37) & 127]
    y -= (res[0] << 14) + (res[1] << 11) + (res[2] << 9)
    y %= 1 << 63
    res = [y >> 56, (y >> 28) & 127, (y >> 18) & 127] + res
    print(*res)
    input()
