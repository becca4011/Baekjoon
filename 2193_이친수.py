import sys

li = [1, 1]
for i in range(2, 91):
    li.append(li[i - 2] + li[i - 1])

N = int(sys.stdin.readline())
print(li[N - 1])
