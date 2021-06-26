import sys

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

dt = dict()
for i in range(N):
    dt[i] = 0

cnt = 0
n = 0
while(True):
    for i in range(N):
        if p[i] != 0:
            p[i] = p[i] - 1
            cnt += 1
        if p[i] == 0 and dt[i] == 0:
            dt[i] = cnt
            n += 1

    if n == N:
        break

for i in range(N):
    print(dt[i], end= " ")