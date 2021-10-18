import sys

N, M = map(int, sys.stdin.readline().split())

S = dict()
for i in range(N):
    S[sys.stdin.readline().rstrip()] = i

cnt = 0
for i in range(M):
    st = sys.stdin.readline().rstrip()
    if st in S:
        cnt += 1

print(cnt)
