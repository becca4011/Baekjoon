import sys


def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            for j in range(i * i, n, i):
                if n % j == 0:
                    return False
        return True


N = int(sys.stdin.readline())

if prime:
    print()
else:
    print(N - 1)
