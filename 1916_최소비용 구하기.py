import sys
import heapq

INF = int(1e9) # 무한을 의미 (10억)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

distance = [INF] * (N + 1) # 최단거리 테이블
graph = [[] for i in range(N + 1)] # 노드 연결정보

for i in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))

start, end = map(int, sys.stdin.readline().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q) # 가장 최단거리가 짧은 노드에 대한 정보 꺼냄
        
        # 이미 처리된 노드 -> 무시
        # 별도의 visited 테이블 필요 X, 최단거리 테이블을 이용해서 방문여부 확인
        if distance[now] < dist:
            continue
        
        # 선택된 노드와 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]: # 선택된 노드를 거쳐서 이동하는 것이 더 빠른 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[end])