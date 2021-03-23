import sys # 시간초과 해결
N = int(sys.stdin.readline())

li = []
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

li = sorted(li, key = lambda li : (li[1], li[0])) # 다중 조건 (li[1]로 먼저 정렬, 그 후에 li[0]로 정렬)

for i in li:
    print(i[0], i[1])