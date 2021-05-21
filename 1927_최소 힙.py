import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
que = PriorityQueue()

for i in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if que.empty():
            print(0)
        else:
            print(que.get())
    else:
        que.put(x)