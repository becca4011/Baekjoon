import sys

M = int(sys.stdin.readline())

s = [0] * 20 # 비트마스킹

for i in range(M):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "add":
        s[int(cmd[1]) - 1] = 1

    elif cmd[0] == "remove":
        s[int(cmd[1]) - 1] = 0
    
    elif cmd[0] == "check":
        if s[int(cmd[1]) - 1] == 1:
            print(1)
        else:
            print(0)

    elif cmd[0] == "toggle":
        if s[int(cmd[1]) - 1] == 1:
            s[int(cmd[1]) - 1] = 0
        else:
            s[int(cmd[1]) - 1] = 1

    elif cmd[0] == "all":
        s = [1] * 20
        # for문으로 넣어주면 시간초과

    elif cmd[0] == "empty":
        s = [0] * 20

"""
import sys

M = int(sys.stdin.readline())

s = set()

for i in range(M):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "add":
        s.add(int(cmd[1]))

    elif cmd[0] == "remove":
        s.discard(int(cmd[1]))
    
    elif cmd[0] == "check":
        if int(cmd[1]) in s:
            print(1)
        else:
            print(0)

    elif cmd[0] == "toggle":
        if int(cmd[1]) in s:
            s.discard(int(cmd[1]))
        else:
            s.add(int(cmd[1]))

    elif cmd[0] == "all":
        s = set([i for i in range(1, 21)])

    elif cmd[0] == "empty":
        s = set()
"""