import sys

n, x = sys.stdin.readline().split()

nums = sys.stdin.readline().split()

for i in nums:
    if (int(i) < int(x)):
        print(i, end=" ")