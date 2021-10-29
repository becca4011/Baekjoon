import sys


def binary(data, find):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == find:
            return "1"
        elif data[mid] < find:
            left = mid + 1
        elif data[mid] > find:
            right = mid - 1

    return "0"


N = int(sys.stdin.readline())
card_N = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
card_M = list(map(int, sys.stdin.readline().split()))

res = list()
for i in card_M:
    res.append(binary(card_N, i))

for i in res:
    print(i, end=" ")
