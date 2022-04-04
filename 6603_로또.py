from shlex import join
import sys
from itertools import combinations

comb = list()
while True:
    S = list(map(int, sys.stdin.readline().split()))
    if S[0] == 0:
        break
    
    comb.append(list(combinations(S[1:], 6)))
    
for i in range(len(comb)):
    for j in comb[i]:
        print(' '.join([str(a) for a in j]))
    print()