import sys

N = int(sys.stdin.readline())
li = list()
for i in range(N):
    li.append(int(sys.stdin.readline()))

li.sort(reverse=True)

res = 0
for i in range(N):
    tip = li[i] - i
    if tip <= 0:
        res += 0
    else:
        res += tip

print(res)
