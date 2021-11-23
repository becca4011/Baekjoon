import sys

N = int(sys.stdin.readline())
li = list()
for i in range(N):
    li.append(int(sys.stdin.readline()))

li.sort(reverse=True)

res = 0
cnt = 0
for i in range(N):
    cnt += 1
    if cnt != 3:
        res += li[i]
    else:
        cnt = 0
print(res)
