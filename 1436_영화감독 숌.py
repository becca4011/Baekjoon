N = int(input())

cnt = 0
n = 0
while (True):
    n += 1
    if str(n).find("666", 0) != -1:
        cnt += 1
    if cnt == N:
        print(n)
        break
