import sys

N, M, B = map(int, sys.stdin.readline().split()) # 땅 크기, 가지고 있는 블럭의 수
ground = []

max = -1
min = 257
for i in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))
    for j in ground[i]:
        if max < j:
            max = j
        if min > j:
            min = j

min_time = 9999999999999999
block_height = 0
for i in range(min, max + 1): # min부터 max까지 돌림
    time = 0
    block = B
    for j in range(N):
        for k in range(M):
            height = ground[j][k] - i # 높이 판정 (쌓거나, 캐거나 둘 중 하나)
            #print(i, ground[j][k], height)
            if height > 0:
                time += height * 2 # 블럭 캐기
                block += height
            elif height < 0:
                time -= height # 블럭 쌓기
                block += height # 0보다 작으므로 더하면 자동으로 빼짐

    if block >= 0: # 인벤토리에 있는 블럭이 0보다 작으면 안됨
        if time <= min_time:
            min_time = time
            block_height = i

    #print(i, time, block, min_time)

print(min_time, block_height)