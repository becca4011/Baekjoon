import sys

T = int(sys.stdin.readline())

for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    x, y = x - 1, y - 1
    k = x

    while k < M * N:
        if k % N == y:
            print(k + 1)
            break
        k += M

    if k % N != y:
        print(-1)