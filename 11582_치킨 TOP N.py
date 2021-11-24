import sys

N = int(sys.stdin.readline())
taste = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
res = list()

for i in range(K):
    res = list()
    for j in range(0, N // (i + 1), 2):
        print(i, j, K)
        save = sorted(taste[j : j + K])
        print(save)
        for l in save:
            res.append(l)
    taste = list(res)
    print(taste)
print(res)
