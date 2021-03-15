c = int(input())

for i in range(c):
    istc = list(map(int, input().split()))
    avg = sum(istc[1:]) / istc[0]
    cnt = 0

    for j in istc[1:]:
        if(avg < j):
            cnt += 1

    print("{:.3f}%".format(100 / istc[0] * cnt))
    #print(str("%.3f" %round(cnt / istc[0] * 100, 3))+"%")