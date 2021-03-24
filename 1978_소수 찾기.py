import sys

N = int(sys.stdin.readline())
Nnum = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in Nnum:
    ic = 0
    for j in range(1, i + 1):
        if i % j == 0:
            ic += 1

    if ic == 2 and i != 1:
        cnt += 1

print(cnt)