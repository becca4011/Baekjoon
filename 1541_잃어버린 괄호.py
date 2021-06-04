import sys

N = sys.stdin.readline().rstrip().split('-')
res = 0

for i in range(len(N)):
    plus = list(map(int, N[i].split('+')))
    
    if len(plus) > 1:
        N[i] = sum(plus)
    else:
        N[i] = plus[0]

    if i == 0:
        res = N[i]
    else:
        res -= N[i]

print(res)