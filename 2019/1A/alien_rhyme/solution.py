def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


def cpl(a, b):
    res = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            res += 1
        else:
            break
    return res


t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    names = list(sorted(input()[::-1] for _ in range(n)))
    cl = [cpl(*names[i:i + 2]) for i in range(len(names) - 1)]
    prefixes = set()
    res = 0
    while any(cl):
        l, maxi = max((x, i) for i, x in enumerate(cl))
        a = names[maxi]
        while a[:l] in prefixes:
            l -= 1
        if l == 0:
            cl[maxi] = 0
        else:
            res += 2
            prefixes.add(a[:l])
            del names[maxi:maxi + 2]
            del cl[maxi]
            if len(cl) > maxi:
                del cl[maxi]
                if maxi > 0:
                    cl[maxi - 1] = cpl(names[maxi - 1], names[maxi])
            elif maxi > 0:
                del cl[maxi - 1]

    printf("Case #{}: {}".format(ti, res))
