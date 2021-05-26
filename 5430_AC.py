import sys
from collections import deque

# 출력을 형식에 맞게 해야 함
def prt(x):
    print("[", end="")
    for k in range(len(x) - 1):
        print(x[k], end=",")
    print(str(x[len(x) - 1]) + "]")

T = int(sys.stdin.readline())

for i in range(T):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().rstrip()
    if x != "[]":
        x = deque(map(int, x[1:len(x)-1].split(",")))
    else:
        x = deque()

    reverse = False
    for j in p:
        if j == 'R':
            reverse = not reverse
        
        if j == 'D' and len(x) != 0:
            if reverse:
                x.pop()
            else:
                x.popleft()
        elif j == 'D' and len(x) == 0:
            print("error")
            break

    else:
        if len(x) == 0:
            print("[]")
        elif not reverse:
            prt(x)
        else:
            x.reverse()
            prt(x)