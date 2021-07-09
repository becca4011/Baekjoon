import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
max_money = int(sys.stdin.readline())

start, end = 0, max(li)

if sum(li) <= max_money:
    print(end)
else:
    while start <= end:
        mid = (start + end) // 2

        total = 0
        for i in li:
            total += min(i, mid)

        if total > max_money:
            end = mid - 1
        else:
            start = mid + 1
    print(end)
