import sys

K = int(sys.stdin.readline())
size = 0
c = 0
while size < K:
    size = 2 ** c
    c += 1

N = size

cnt = 0
while K > 0:
    if K >= size:
        K -= size
    else:
        size //= 2
        cnt += 1

print(N, cnt)
