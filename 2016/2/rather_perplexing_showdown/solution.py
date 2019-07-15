import sys

filename = "A-large-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    n, r, p, s = [int(x) for x in input().split(" ")]
    groups = [["R" for _ in range(r)], ["P" for _ in range(p)], ["S" for _ in range(s)]]
    impossible = False
    for i in range(n):
        rp, ps, sr = (r + p - s) // 2, (p + s - r) // 2, (r + s - p) // 2
        if max(rp, sr) > r or max(rp, ps) > p or max(ps, sr) > s:
            impossible = True
            break
        ngroups = [[], [], []]
        for _ in range(rp):
            ngroups[1].append(groups[0].pop() + groups[1].pop())
        for _ in range(ps):
            ngroups[2].append(groups[2].pop() + groups[1].pop())
        for _ in range(sr):
            ngroups[0].append(groups[0].pop() + groups[2].pop())
        groups = ngroups
        r, p, s = sr, rp, ps
    if impossible:
        printf("Case #{}: IMPOSSIBLE".format(ti))
        continue
    final = ""
    for group in groups:
        if group:
            final = group[0]
    for i in range(n):
        csize = 2 ** (i + 1)
        nfinal = []
        for j in range(2 ** (n - i - 1)):
            first = final[j * csize:((j + 1) * csize) - (csize // 2)]
            second = final[((j + 1) * csize) - (csize // 2):(j + 1) * csize]
            if first < second:
                nfinal.append(first)
                nfinal.append(second)
            else:
                nfinal.append(second)
                nfinal.append(first)
        final = "".join(nfinal)
    printf("Case #{}: {}".format(ti, final))