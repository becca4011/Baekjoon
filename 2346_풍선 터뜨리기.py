import sys
from collections import deque

N = int(sys.stdin.readline())
balloon = deque(map(int, sys.stdin.readline().split()))
dq = deque(range(1, N + 1))
res = list()

while len(res) != N:
    b = balloon.popleft()
    i = dq.popleft()
    res.append(i)

    if b > 0:
        balloon.rotate(-(b - 1))
        dq.rotate(-(b - 1))
    else:
        balloon.rotate(-b)
        dq.rotate(-b)

for i in res:
    print(i, end=" ")
