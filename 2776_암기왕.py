import sys


def binary(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return "1"
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return "0"


T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    li_n = list(map(int, sys.stdin.readline().split()))
    dt_n = {j: li_n[j] for j in range(N)}

    M = int(sys.stdin.readline())
    li_m = list(map(int, sys.stdin.readline().split()))
    dt_m = {j: li_m[j] for j in range(M)}

    # s_n = sorted(dt_n.items(), key=(lambda x: x[1]), reverse=True)
    item_m = sorted(dt_m.items(), key=(lambda x: x[1]))

    s_n = sorted(dt_n.values())

    dt = dict()
    for i in range(M):
        dt[i] = binary(li_m[i], s_n)

    for i in dt.values():
        print(i)
