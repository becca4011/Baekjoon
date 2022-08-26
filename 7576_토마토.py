import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

box = list()
for i in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))

dq = deque([])

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1: # 익은 토마토
            dq.append([i, j])
        
def bfs():
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx >= 0 and nx < N and ny >= 0 and ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                dq.append([nx, ny])
            
bfs()

day = 0
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))
    
print(day - 1)