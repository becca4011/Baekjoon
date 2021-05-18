import sys

N, K = map(int, sys.stdin.readline().split())
A = list()

for i in range(N):
    A.append(int(sys.stdin.readline()))

A.reverse()
sum = 0
for i in A:
    if i > K:
        continue
    sum += K // i
    K -= (K // i) * i

print(sum)