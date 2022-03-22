import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num = sorted(num)
num = sorted(set(list(combinations(num, M))))

for i in range(len(num)):
    for j in range(len(num[i])):
        print(num[i][j], end=" ")
    print()