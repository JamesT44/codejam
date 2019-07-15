def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    a = int(input())
    boxes = (a + 8) // 9
    for i in range(boxes):
        done = set()
        middle = 3 * i + 2
        while len(done) < 9:
            printf(middle, 2)
            x, y = map(int, input().split())
            if x == y == 0:
                break
            done.add((x, y))
        else:
            continue
        break