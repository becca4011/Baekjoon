import sys

nA, nB = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

res = sorted(list(A - B))
print(len(res))
for i in res:
    print(i, end=" ")
