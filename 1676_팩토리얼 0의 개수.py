import sys
import math

N = int(sys.stdin.readline())
f = list(str(math.factorial(N)))
f.reverse()

cnt = 0
for i in f:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)