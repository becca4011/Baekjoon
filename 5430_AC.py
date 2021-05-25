# 미해결
import sys

T = int(sys.stdin.readline())

for i in range(T):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().rstrip()
    if x != "[]":
        x = list(map(int, x[1:len(x)-1].split(",")))
    else:
        print("error")
        continue

    prv = ""
    for j in p:
        if j == 'R' and prv != 'R':
            x.reverse()
            prv = ""
            #print("A :", x)
        else:
            prv = p
        
        if j == 'D' and len(x) != 0:
            x.pop(0)
            #print("B :", x)
        elif len(x) == 0:
            break
        #print(prv)

    if len(x) == 0:
        print("error")
    else:
        print(x)