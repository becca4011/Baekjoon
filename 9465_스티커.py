import sys

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    sticker = list()
    for i in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))
    
    cnt = 0
    zo = 0
    res = list()
    for i in range(len(sticker[0]) - 1):
        if i == len(sticker[0]) - 2:
            if zo == 0:
                res.append(max(sticker[1][i], sticker[0][i + 1], sticker[1][i + 1]))
                cnt += max(sticker[1][i], sticker[0][i + 1], sticker[1][i + 1])
            elif zo == 1:
                res.append(max(sticker[0][i], sticker[0][i + 1], sticker[1][i + 1]))
                cnt += max(sticker[0][i], sticker[0][i + 1], sticker[1][i + 1])
        else:
            if sticker[0][i] > sticker[1][i]:
                cnt += sticker[0][i]
                zo = 0
                res.append(sticker[0][i])
            elif sticker[0][i] < sticker[1][i]:
                cnt += sticker[1][i]
                zo = 1
                res.append(sticker[1][i])
    print(cnt)
    print(res)