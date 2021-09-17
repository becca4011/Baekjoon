import sys

N, Q = map(int, sys.stdin.readline().split())
A = sorted(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    A[i] = A[i - 1] + A[i]  # 누적 합

for i in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    if L == 1:
        print(A[R - 1])
    else:
        print(A[R - 1] - A[L - 2])
