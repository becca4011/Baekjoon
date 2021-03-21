N = int(input())

li = []
for i in range(N):
    li.append(list(map(int, input().split())))

for i in range(N):
    point = 1
    for j in range(N):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            point += 1

    print(point, end = " ")