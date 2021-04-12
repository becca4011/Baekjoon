import sys

M = int(sys.stdin.readline())

s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 비트마스킹

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
        s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # for문으로 넣어주면 시간초과

    elif cmd[0] == "empty":
        s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]