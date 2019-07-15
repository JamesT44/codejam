def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(t):
    a, b = [int(x) for x in input().split(" ")]
    a += 1
    n = int(input())
    while True:
        guess = (a + b) // 2
        printf(guess)
        result = input()
        if result == "CORRECT":
            break
        elif result == "TOO_BIG":
            b = guess - 1
        elif result == "TOO_SMALL":
            a = guess + 1
