import sys

deque = list()

N = int(sys.stdin.readline())

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front":
        deque.insert(0, int(cmd[1]))
    
    elif cmd[0] == "push_back":
        deque.append(int(cmd[1]))

    elif cmd[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    
    elif cmd[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(len(deque) - 1))

    elif cmd[0] == "size":
        print(len(deque))

    elif cmd[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif cmd[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque) - 1])