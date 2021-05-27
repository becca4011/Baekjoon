# 미해결
import sys
from queue import PriorityQueue

T = int(sys.stdin.readline())

for i in range(T):
    que_min = PriorityQueue()
    que_max = PriorityQueue()

    k = int(sys.stdin.readline())
    for j in range(k):
        Q = sys.stdin.readline().split()

        if Q[0] == "I":
            que_min.put(int(Q[1]))
            que_max.put(-1 * int(Q[1]))
        elif Q[0] == "D":
            if que_min.empty() and que_max.empty():
                continue
            if int(Q[1]) == -1:
                que_min.get()
            else:
                que_max.get()

    mx = -1 * min(que_max.queue)
    mn = min(que_min.queue)

    if mx == mn:
        print("EMPTY")
    else:
        print(mx, mn)