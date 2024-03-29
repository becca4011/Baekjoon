import sys

N = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().split()))

dt = dict()
res = dict()
for i in range(N):
    dt[i] = height[i]
    res[i] = -1
    
for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == dt[i] and res[j] == -1:
            res[j] = i
            break
        if res[j] == -1 and cnt != dt[i]:
            cnt += 1

for i in range(N):
    print(res[i] + 1, end=" ")

"""
2 1 1 0
1 2 3 4

-1 -1 -1 -1
-1 -1 1 -1
-1 2 1 -1
-1 2 1 3
4 2 1 3
-------------------------------
6 1 1 1 2 0 0
1 2 3 4 5 6 7

-1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 1
-1 2 -1 -1 -1 -1 1
-1 2 3 -1 -1 -1 1
-1 2 3 4 -1 -1 1
-1 2 3 4 -1 5 1
6 2 3 4 -1 5 1
6 2 3 4 7 5 1
-------------------------------
5 3 7 1 4 2 1 0 0 0
1 2 3 4 5 6 7 8 9 10

-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 1 -1 -1 -1 -1
-1 -1 -1 2 -1 1 -1 -1 -1 -1
-1 -1 -1 2 -1 1 -1 -1 -1 3 (-1 7번 지나친 후 그 자리에 입력)
-1 4 -1 2 -1 1 -1 -1 -1 3
-1 4 -1 2 -1 1 -1 5 -1 3
-1 4 -1 2 6 1 -1 5 -1 3
-1 4 7 2 6 1 -1 5 -1 3
8 4 7 2 6 1 -1 5 -1 3
8 4 7 2 6 1 9 5 -1 3
8 4 7 2 6 1 9 5 10 3
"""