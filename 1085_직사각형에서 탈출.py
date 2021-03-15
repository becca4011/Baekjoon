coo = input().split()

# coo[0] = x / coo[1] = y / coo[2] = w / coo[3] = h
# (0, 0)과 (w, h)중 어디가 가까운지 알아봐야 함
# x - 0, w - x를 비교 / y - 0, h - y를 비교 후 작은 것을 또 비교

wx = int(coo[2]) - int(coo[0])
hy = int(coo[3]) - int(coo[1])

max1 = int(coo[0]) if int(coo[0]) < wx else wx
max2 = int(coo[1]) if int(coo[1]) < hy else hy

if max1 < max2:
    print(max1)
else:
    print(max2)