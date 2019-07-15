import sys

filename = "A-small-practice"
sys.stdin = open(filename + ".in", "r")
sys.stdout = open(filename + ".out", "w")


def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


mapping = "yhesocvxduiglbkrztnwjpfmaq"
t = int(input())
for ti in range(1, t + 1):
    g = input()
    printf("Case #{}: {}".format(ti, "".join(" " if c == " " else mapping[ord(c) - ord("a")] for c in g)))
