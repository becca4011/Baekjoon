import sys

def binary(left, right, find):
    while (left <= right):
        mid = (left + right) // 2
        if A[mid] == find:
            return 1
        elif A[mid] < find:
            left = mid + 1
        elif A[mid] > find:
            right = mid - 1
    return 0

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A = sorted(A)

M = int(sys.stdin.readline())
Mnum = list(map(int, sys.stdin.readline().split()))


for find in Mnum:
    print(binary(0, N - 1, find))