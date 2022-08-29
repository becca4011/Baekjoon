import sys
sys.setrecursionlimit(10**6)

def dfs(a):
    # 체크인
    visited[a] = True
    
    # 연결된 곳을 순회
    for i in graph[a]:
        # 갈 수 있는가?
        if not visited[i]:
            # 간다
            dfs(i)
    return

N, M = map(int, sys.stdin.readline().split())

visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i)
            cnt += 1
            
print(cnt)