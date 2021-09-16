import sys
from queue import PriorityQueue

que = PriorityQueue()
n = int(sys.stdin.readline())
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))

    if len(a) > 1:
        for j in range(1, len(a)):
            que.put(-a[j])
    else:
        if que.empty():
            print(-1)
        else:
            print(-que.get())
