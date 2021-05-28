# 미해결
import sys
import heapq

def pop(que, visited):
    while que and not visited[que[0][1]]:
        heapq.heappop(que)

T = int(sys.stdin.readline())

for i in range(T):
    que_min = []
    que_max = []
    visited = [False] * 1000000

    k = int(sys.stdin.readline())
    for j in range(k):
        Q = sys.stdin.readline().split()

        if Q[0] == "I":
            heapq.heappush(que_min, (int(Q[1]), j))
            heapq.heappush(que_max, (-1 * int(Q[1]), j))
            visited[j] = True
        elif Q[0] == "D":
            if Q[1] == "-1":
                pop(que_min, visited)
                if que_min:
                    visited[que_min[0][1]] = False
                    heapq.heappop(que_min)
            elif Q[1] == "1":
                pop(que_max, visited)
                if que_max:
                    visited[que_max[0][1]] = False
                    heapq.heappop(que_max)

    pop(que_max, visited)
    pop(que_min, visited)

    if que_max:
        print(-que_max[0][0], que_min[0][0])
    else:
        print("EMPTY")