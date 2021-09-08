import sys
from collections import deque

N, K, M = map(int, sys.stdin.readline().split())

josephus = deque(range(1, N + 1))

b = False
r = -(K - 1)
li = list()
while len(josephus) != 0:
    if len(li) % M == 0 and len(li) >= M:
        if not b:
            b = True
            r = K
        elif b:
            b = False
            r = -(K - 1)  # K - 1번 돌면 반대로 돌아야 함

    josephus.rotate(r)  # list 회전 (r만큼 회전하면 그 사람은 제거될 사람)
    li.append(josephus.popleft())

for i in li:
    print(i)
