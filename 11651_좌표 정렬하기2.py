import sys # 시간초과 해결
N = int(sys.stdin.readline())

li = []
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

li = sorted(li, key = lambda li : (li[1], li[0]))

for i in li:
    print(i[0], i[1])