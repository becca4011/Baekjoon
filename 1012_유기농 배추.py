import sys
from collections import deque

def bfs(graph, a, b):
    dq = deque([])
    dq.append([a, b])
    graph[a][b] = 0
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx >= 0 and nx < M and ny >= 0 and ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dq.append([nx, ny])
    return

T = int(sys.stdin.readline())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0] * N for _ in range(M)]
    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X][Y] = 1

    cnt = 0

    for j in range(M):
        for k in range(N):
            if graph[j][k] == 1:
                bfs(graph, j, k)
                cnt += 1
    print(cnt)