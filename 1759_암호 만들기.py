import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
word = sys.stdin.readline().split()

vowel = list()
cons = list()

for i in word:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowel.append(i)
    else:
        cons.append(i)
        
comb = list(combinations(word, L))
res = list()

for i in comb:
    vcnt = 0
    ccnt = 0
    for j in i:
        if j in vowel:
            vcnt += 1
        else:
            ccnt += 1
    if vcnt >= 1 and ccnt >= 2:
        t = tuple(sorted(i))
        res.append("".join(t))
    
res = sorted(set(res))

for i in res:
    print(i)