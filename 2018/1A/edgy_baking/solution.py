from bisect import insort


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, p = map(int, input().split())
    cookies = [tuple(map(int, input().split())) for _ in range(n)]
    s = sum(2 * w + 2 * h for w, h in cookies)
    intervals = [[s, s]]
    for w, h in cookies:
        l, r = 2 * min(w, h), 2 * ((w * w + h * h) ** 0.5)
        for la, ra in intervals[:]:
            insort(intervals, [la + l, ra + r])
        ni = [intervals[0]]
        for l, r in intervals[1:]:
            if l > p:
                break
            if l <= ni[-1][-1]:
                ni[-1][-1] = max(ni[-1][-1], r)
            else:
                ni.append([l, r])
        intervals = ni
    printf("Case #{}: {:0.7f}".format(ti, min(p, intervals[-1][-1])))
