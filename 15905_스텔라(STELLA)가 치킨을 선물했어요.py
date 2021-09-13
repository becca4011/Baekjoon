import sys

li = list()
N = int(sys.stdin.readline())
for i in range(N):
    cn, pa = map(int, sys.stdin.readline().split())
    li.append([cn, pa])

li.sort(key=lambda x: (-x[0], x[1]))
cnt = 0
if len(li) > 5:
    for i in range(5, N):
        if li[4][0] == li[i][0]:
            cnt += 1

print(cnt)
