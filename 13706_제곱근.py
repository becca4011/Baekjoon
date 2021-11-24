import sys


def binary(target):
    start = 0
    end = target

    while start <= end:
        mid = (start + end) // 2

        if mid ** 2 == target:
            return mid
        elif mid ** 2 < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(sys.stdin.readline())
print(binary(N))
