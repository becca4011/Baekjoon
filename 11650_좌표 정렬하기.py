import sys # 시간초과 해결
N = int(sys.stdin.readline())

li = []
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

li = sorted(li)

for i in li:
    print(i[0], i[1])