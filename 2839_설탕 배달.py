gram = int(input())

cnt = 0
while (True):
    if gram > 0:
        if gram % 5 != 0:
            gram -= 3
            cnt += 1
        elif gram % 5 == 0:
            cnt += gram // 5
            gram = gram % 5
        else:
            print(-1)
            break
    else:
        print(-1)
        break

    if gram == 0:
        print(cnt)
        break