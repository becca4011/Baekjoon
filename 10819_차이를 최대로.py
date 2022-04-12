import sys
from itertools import permutations

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

perm = list(permutations(A, N))

max = -1
for i in perm:
    res = 0
    for j in range(N - 1):
        res += abs(i[j] - i[j + 1])
    
    if max < res:
        max = res
        
print(max)