import sys

N = int(sys.stdin.readline())
li = list()
for i in range(N):
    li.append(int(sys.stdin.readline()))

li.sort()

cnt = 0
for i in range(N):
    if i + 1 != li[i]:
        cnt += abs(li[i] - (i + 1))

print(cnt)
