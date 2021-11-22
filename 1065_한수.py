import sys

N = int(sys.stdin.readline())

cnt = 0
for i in range(1, N + 1):
    if i < 100:
        cnt += 1
    else:
        li = list(map(int, list(str(i))))
        s = li[1] - li[0]
        for i in range(1, len(li) - 1):
            if s != li[i + 1] - li[i]:
                break
            cnt += 1
print(cnt)
