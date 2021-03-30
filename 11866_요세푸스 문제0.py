import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

josephus = deque()
for i in range(N):
    josephus.append(i + 1)

cnt = 1
li = list()
while(len(josephus) != 0):
    j = josephus.popleft()
    if cnt != K:
        josephus.append(j)
    else:
        li.append(j)
        cnt = 0
    cnt += 1

print("<", end="")
for i in li:
    if i == li[-1]:
        print(i, end="")
    else:
        print(i, end=", ")
print(">")