import sys


def prime():
    n = 1000000
    p = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if p[i] == True:
            for j in range(i + i, n, i):
                p[j] = False
    return p


N = int(sys.stdin.readline())
A = map(int, sys.stdin.readline().split())
P = prime()

res = 1
cnt = 0
dt = dict()
for i in A:
    if P[i] == True and i not in dt:
        res *= i
        dt[i] = 0
        cnt += 1

if cnt != 0:
    print(res)
else:
    print(-1)
