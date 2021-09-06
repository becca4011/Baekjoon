import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    cd = dict()
    for i in range(N + M):
        cd_num = int(sys.stdin.readline())
        cd[cd_num] = cd.get(cd_num, 0) + 1

    cnt = 0
    for v in cd.values():
        if v == 2:
            cnt += 1
    print(cnt)
