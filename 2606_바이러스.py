import sys


visited = list()
cnt = 0


def DFS(graph, root):
    visited.append(root)
    global cnt

    for v in graph[root]:
        if v not in visited:
            visited.append(v)
            cnt += 1
            DFS(graph, v)


com = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

graph = dict()
for i in range(pair):
    n1, n2 = map(int, sys.stdin.readline().split())

    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

DFS(graph, 1)
print(cnt)
