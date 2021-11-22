import sys


def prime(n):
    dt = dict()
    p = 2
    while p <= n:
        if n % p == 0:
            dt[p] = dt.get(p, 0) + 1
            n /= p
        else:
            p += 1

    for k, v in dt.items():
        print(k, v)


T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    prime(N)
