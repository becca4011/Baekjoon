import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

all_li = list()
for i in range(1, N + 1):
    all_li += list(combinations(li, i))

cnt = 0
for i in all_li:
    if sum(i) == S:
        cnt += 1
        
print(cnt)