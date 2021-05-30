import sys
from collections import deque

T = int(sys.stdin.readline())
que = deque()

for i in range(T):
    N = sys.stdin.readline().split()

    if N[0] == "push":
        que.append(int(N[1]))
    elif N[0] == "pop":
        print(que.popleft() if len(que) != 0 else -1)
    elif N[0] == "size":
        print(len(que))
    elif N[0] == "empty":
        print(0 if len(que) != 0 else 1)
    elif N[0] == "front":
        print(que[0] if len(que) != 0 else -1)
    elif N[0] == "back":
        print(que[len(que) - 1] if len(que) != 0 else -1)