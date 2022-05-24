import sys
from collections import deque

st = sys.stdin.readline().rstrip()

dq = deque()
tmp = 1
res = 0
for i in range(len(st)):
    if st[i] == '(':
        dq.append(st[i])
        tmp *= 2
    elif st[i] == '[':
        dq.append(st[i])
        tmp *= 3
    elif st[i] == ')':
        if not dq or dq[-1] == '[':
            res = 0
            break
        if st[i - 1] == '(':
            res += tmp
        dq.pop()
        tmp //= 2
    elif st[i] == ']':
        if not dq or dq[-1] == '(':
            res = 0
            break
        if st[i - 1] == '[':
            res += tmp
        dq.pop()
        tmp //= 3

if len(dq) == 0:
    print(res)
else:
    print(0)